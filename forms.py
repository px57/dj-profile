import email
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext as _
from django.utils.deconstruct import deconstructible
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms

from kernel.http.serialize import user

from profiles.models import VerifyIdentifier
from .validators import PasswordFields, FirstOrLastNameValidator
from profiles import models as profile_models
from django.db.models import Q


import uuid

class LoginForm(forms.Form):
    """
        Recept the new user info.
    """
    
    username = forms.EmailField(required=True)
    password = PasswordFields(required=True)
    
    def clean_username(self):
        """Validate the username values."""
        username = self.cleaned_data.get('username')
        if not User.objects.filter(email=username): 
            raise ValidationError(
                _("email_exists"),
                code='email_exists',
            )
        return username

class SignupUserForm(forms.ModelForm):
    """Recept the new user info."""
    class Meta:
        fields = ['username', 'email', 'password']
        model = User

    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    password = PasswordFields(required=True)
    username = forms.CharField(required=False)

    def clean_email(self):
        """Validation de l'email."""
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise ValidationError(
                _("email_exists"),
                code='email_exists',
            )
        return email

    def clean_username(self):
        """Validate the username values."""
        username = self.cleaned_data.get('username')
        username = uuid.uuid4().hex
        return username
    
class ForgotPasswordForm(forms.Form):
    """Recept the new user info."""
    class Meta:
        fields = ['email']
        # model = User

    email = forms.EmailField(required=True)

    def clean_email(self):
        """Validation de l'email."""
        email = self.cleaned_data.get('email')
        dbProfile = profile_models.Profile.objects.filter(user__email=email)
        if not dbProfile.exists():
            raise ValidationError(
                _("account_not_found"),
                code='account_not_found',
            )
        return dbProfile.first()

class ResetPasswordVerifyTokenForm(forms.Form):
    """Recept the new user info."""
    class Meta:
        fields = ['token']
        
    token = forms.CharField(max_length=32, required=True)

    def clean_token(self):
        """Validation du token."""
        token = self.cleaned_data.get('token')
        dbToken = profile_models.ResetPasswordModels.objects.filter(token=token)
        if not dbToken.exists():
            raise ValidationError(
                _("token_dont_exists"),
                code='token_dont_exists',
            )
        
        if dbToken.first().status != 'NEW':
            raise ValidationError(
                _("token_expired"),
                code='token_expired',
            )
        
        return dbToken.first()

class ResetPasswordForm(forms.Form):
    """Recept the new user info."""
    class Meta:
        fields = ['password']
        

    password = PasswordFields(required=True)
    confirm_password = forms.CharField(max_length=250)
    
    def clean_repeat_password(self):
        """Validation du repeat_password."""
        repeat_password = self.cleaned_data.get('repeat_password')
        password = self.cleaned_data.get('password')
        
        if repeat_password != password:
            raise ValidationError(
                _("token_exists"),
                code='token_exists',
            )
        return repeat_password
    
class EditProfileForm(forms.Form):
    """Recept the new user info."""
    username = forms.CharField(max_length=250, required=True)
    avatar = forms.CharField(max_length=250, required=False)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=250, required=True)
    last_name = forms.CharField(max_length=250, required=True)
    
    def clean_username(self):
        """_summary_"""
        username = self.cleaned_data.get('username')
        dbUser = User.objects.filter(username=username)
        if not dbUser.exists():
            raise ValidationError(
                _("token_exists"),
                code='token_exists',
            )
        return dbUser.first()

    def clean_email(self):
        """Validation de l'email."""
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        dbUser = User.objects.filter(~Q(username=username.username), email=email)
        
        if dbUser.exists():
            raise ValidationError(
                _("email_exists"),
                code='email_exists',
            )
        return email

class VerifyIdentifierForm(forms.Form):
    """
        @description: 
    """

    token = forms.CharField(max_length=32, required=True)

    def clean_token(self):
        """
            @description: 
        """
        token = self.cleaned_data.get('token')
        dbVerify = VerifyIdentifier.objects.filter(token=token)
        if not dbVerify.exists():
            raise ValidationError(
                'token_not_exists',
                code='token_not_exists',
            )
        
        if dbVerify.first().status == 'USED':
            raise ValidationError(
                'token_used',
                code='token_used',
            )
        return dbVerify.first()
    