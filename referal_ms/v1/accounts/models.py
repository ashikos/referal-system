from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from common import library as comm_lib


# Create your models here.


class ProjectUser(AbstractUser):

    referral = models.CharField(max_length=200, null=True, blank=True)
    referrer = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='refers')

    def generate_referral_code(self):

        referral_code = comm_lib.generate_referral_code(self.id)
        self.referral = referral_code
        self.save()
        return self.referral


    def __str__(self):
        """Object Name in Django Model."""
        return f'{self.id}: {self.username}- {self.referral}'


