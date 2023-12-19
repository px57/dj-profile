# Generated by Django 4.2 on 2023-10-24 22:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mediacenter', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BreakTimeModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activated', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text="The object's creation date/time", null=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now_add=True, help_text="The object's last update date/time", null=True, verbose_name='updated on')),
                ('last_use', models.DateTimeField()),
                ('key', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-updated_on'],
                'get_latest_by': 'updated_on',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activated', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text="The object's creation date/time", null=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now_add=True, help_text="The object's last update date/time", null=True, verbose_name='updated on')),
                ('group', models.CharField(choices=[('root', 'Admin'), ('player', 'Player')], default='player', max_length=20)),
                ('email_verified', models.BooleanField(default=False)),
                ('is_anonymous', models.BooleanField(default=False)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('settings', models.JSONField(default={})),
                ('language', models.CharField(choices=[('fr', 'Français'), ('en', 'English'), ('es', 'Español'), ('de', 'Deutsch'), ('it', 'Italiano'), ('pt', 'Português'), ('ru', 'Русский'), ('zh', '中文'), ('ja', '日本語'), ('ar', 'العربية'), ('ko', '한국어'), ('hi', 'हिन्दी')], default='en', max_length=10)),
                ('isbotnet', models.BooleanField(default=False)),
                ('avatar', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='avatar', to='mediacenter.filesmodel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_on'],
                'get_latest_by': 'updated_on',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResetPasswordModels',
            fields=[
                ('activated', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text="The object's creation date/time", null=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now_add=True, help_text="The object's last update date/time", null=True, verbose_name='updated on')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='profiles.profile', verbose_name='UID')),
                ('token', models.CharField(max_length=32, unique=True)),
                ('status', models.CharField(choices=[('NEW', 'Nouveaux ticket de récupérations'), ('USED', 'Ticket utilisée')], default='NEW', max_length=30)),
            ],
            options={
                'ordering': ['-updated_on'],
                'get_latest_by': 'updated_on',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VerifyIdentifier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activated', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text="The object's creation date/time", null=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now_add=True, help_text="The object's last update date/time", null=True, verbose_name='updated on')),
                ('token', models.CharField(max_length=32, unique=True)),
                ('status', models.CharField(choices=[('NEW', 'Nouveaux ticket de vérification'), ('USED', 'Ticket utilisée')], default='NEW', max_length=30)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
            options={
                'ordering': ['-updated_on'],
                'get_latest_by': 'updated_on',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NetWorkModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activated', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text="The object's creation date/time", null=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now_add=True, help_text="The object's last update date/time", null=True, verbose_name='updated on')),
                ('url', models.CharField(default='', max_length=250)),
                ('key', models.CharField(choices=[('instagram', 'Instagram'), ('tiktok', 'Tiktok'), ('youtube', 'Youtube'), ('linkedin', 'Linkedin'), ('facebook', 'Facebook'), ('twitter', 'Twitter')], default='', max_length=50)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.profile')),
            ],
            options={
                'ordering': ['-updated_on'],
                'get_latest_by': 'updated_on',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ForgetPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activated', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, help_text="The object's creation date/time", null=True, verbose_name='created on')),
                ('updated_on', models.DateTimeField(auto_now_add=True, help_text="The object's last update date/time", null=True, verbose_name='updated on')),
                ('token', models.CharField(max_length=32)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated_on'],
                'get_latest_by': 'updated_on',
                'abstract': False,
            },
        ),
    ]
