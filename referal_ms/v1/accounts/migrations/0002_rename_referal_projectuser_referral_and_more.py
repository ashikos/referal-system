# Generated by Django 4.2.10 on 2024-04-08 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectuser',
            old_name='referal',
            new_name='referral',
        ),
        migrations.AddField(
            model_name='projectuser',
            name='referrar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='refers', to=settings.AUTH_USER_MODEL),
        ),
    ]
