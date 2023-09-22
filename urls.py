"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        'signin/', 
        views.signin, 
        name='signin'
    ),
    path(
        'signup/', 
        views.signup, 
        name='signup'
    ),
    path(
        'forget-password/', 
        views.forget_password, 
        name='forget-password'
    ),
    path(
        'reset-password-verify-token/', 
        views.reset_password_verify_token, 
        name='reset-password-verify-token'
    ),
    path(
        'reset-password/', 
        views.reset_password, 
        name='reset-password'
    ),
    path(
        'verify-email/',
        views.verify_email,
        name='verify-email'
    ),
    path(
        'me/',
        views.me,
        name='me'
    ),
    path(
        'logout/',
        views.logout,
        name='logout'
    ),
]