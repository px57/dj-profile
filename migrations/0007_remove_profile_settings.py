# Generated by Django 4.2 on 2023-10-19 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_remove_breaktimemodels_settings_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='settings',
        ),
    ]
