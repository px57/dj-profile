# Generated by Django 4.2 on 2023-10-19 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='breaktimemodels',
            name='settings',
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='forgetpassword',
            name='settings',
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='networkmodels',
            name='settings',
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='resetpasswordmodels',
            name='settings',
            field=models.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='verifyidentifier',
            name='settings',
            field=models.JSONField(default={}),
        ),
    ]
