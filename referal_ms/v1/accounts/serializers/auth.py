from rest_framework import serializers
from v1.accounts.models import *
from rest_framework.exceptions import APIException
from rest_framework import exceptions
from django.db import transaction


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    referral_points = serializers.SerializerMethodField(required=False)

    class Meta:
        """Meta info"""
        model = ProjectUser
        fields = "__all__"

    def get_referral_points(self, instance):
        """functions to get referral points"""
        count = instance.refers.all().count()
        return count

    @transaction.atomic()
    def create(self, validated_data):
        """override create to create user to give points to the referrer"""
        email = validated_data['email']
        referrer = None
        if "referral" in validated_data.keys():
            referral_code = validated_data.pop('referral')
            try:
                referrer = ProjectUser.objects.get(referral=referral_code)
            except:
                raise exceptions.NotFound(
                    f"User with referral {referral_code} not found")

        if ProjectUser.objects.filter(username=email).exists():
            raise APIException("Email already existing")
        validated_data["username"] = email
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.generate_referral_code()

        user.referrer = referrer
        user.save()

        return user


class ReferralSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta info"""
        model = ProjectUser
        fields = ["username", "date_joined"]
