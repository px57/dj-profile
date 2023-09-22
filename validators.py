
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.translation import gettext as _
from django.utils.deconstruct import deconstructible
from django.contrib.auth.models import User

from django import forms

import json

FORBIDDEN_FIRSTNAMEANDLASTNAME = [
    'staff',
]
FORBIDDEN_FIRSTNAME = []
FORBIDDEN_LASTNAME = []

FORBIDDEN_FIRSTNAME.extend(FORBIDDEN_FIRSTNAMEANDLASTNAME)
FORBIDDEN_LASTNAME.extend(FORBIDDEN_FIRSTNAMEANDLASTNAME)

class PasswordFields(forms.Field):
    """
        1. Validate if BankInfoId is valide
    """
    default_validators = []

    def __init__(self, load_bank_info=True, required=True):
        super().__init__()
        self.load_bank_info = load_bank_info
        self.required = required

    def to_python(self, password):
        if len(password) == 0:
            raise ValidationError(
                _("required"),
                code='password_min_length'
            )

        if len(password) < 8:
            raise ValidationError(
                _("password_too_short"),
                code='password_min_length'
            )
        
        if len(password) > 128:
            raise ValidationError(
                _("password_too_long"),
                code='password_max_length'
            )
        
        if password.isnumeric():
            raise ValidationError(
                _("password_is_numeric"),
                code='password_is_numeric'
            )
        
        if password.isalpha():
            raise ValidationError(
                _("password_is_alpha"),
                code='password_is_alpha'
            )
        
        if password.islower():
            raise ValidationError(
                _("password_is_lower"),
                code='password_is_lower'
            )

        if ' ' in password:
            raise ValidationError(
                _("password_has_space"),
                code='password_has_space'
            )
        return password


class FirstOrLastNameValidator(forms.Field):
    """
        1. Validate if BankInfoId is valide
    """
    default_validators = []

    def __init__(self, load_bank_info=True, required=True):
        super().__init__()
        self.load_bank_info = load_bank_info
        self.required = required

    def to_python(self, firstOrlast__name):
        return firstOrlast__name

class FirstNameValidator(forms.Field):
    """
        @description: Valider l'email de l'utilisateurs
    """
    default_validators = []

    def __init__(self, load_bank_info=True, required=True):
        super().__init__()
        self.load_bank_info = load_bank_info
        self.required = required

    def to_python(self, firstName):
        """
            @description:
        """
        firstName = firstName.lower()
        if firstName in FORBIDDEN_FIRSTNAME:
            raise ValidationError(
                _("Ce nom est interdit sur Venture Project"),
                code='password_min_length'
            )
        return firstName

class LastNameValidator(forms.Field):
    """
        @description:
    """
    default_validators = []

    def __init__(self, load_bank_info=True, required=True):
        super().__init__()
        self.load_bank_info = load_bank_info
        self.required = required

    def to_python(self, lastname):
        """
            @description:
        """
        lastname = lastname.lower()
        if lastname in FORBIDDEN_LASTNAME:
            raise ValidationError(
                _("Ce prénom est interdit sur Venture Project"),
                code='password_min_length'
            )
        return lastname

