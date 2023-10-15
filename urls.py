"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        'signin/', 
        views.signin, 
        name='profiles__signin'
    ),
    path(
        'signup/', 
        views.signup, 
        name='signup'
    ),
    path(
        'forget-password/', 
        views.forget_password, 
        name='profiles__forget_password'
    ),
    path(
        'reset-password/', 
        views.reset_password, 
        name='profiles__reset_password'
    ),
    path(
        'verify-email/',
        views.verify_email,
        name='profiles__verify_email'
    ),
    path(
        'me/',
        views.me,
        name='profiles__me'
    ),
    
    path(
        'logout/',
        views.logout,
        name='profiles__logout'
    ),
    path(
        'update-password/',
        views.update_password,
        name='profiles__update_password'
    ),

    path(
        'update_profile/',
        views.update_profile,
        name='profiles__update_profile'
    )
]