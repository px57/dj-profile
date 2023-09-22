from kernel.http import Response
from kernel.http.decorators import load_json

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from profiles import forms as profile_forms
from profiles import models as profile_models
from profiles import libs as profile_libs


def signup_anonymous_profile(dbProfile, cleaned_data):
    """
        @description: 
    """
    res = Response()
    dbProfile.user.username = cleaned_data['username']
    dbProfile.user.email = cleaned_data['email']
    dbProfile.user.first_name = cleaned_data['first_name']
    dbProfile.user.last_name = cleaned_data['last_name']
    dbProfile.is_anonymous = False
    dbProfile.user.set_password(cleaned_data['password'])

    dbProfile.user.save()
    dbProfile.save()

    dbVerify = profile_libs.generate_verify_token(dbProfile)
    profile_libs.send_verify_token_with_email(dbVerify)

    res.DEV = {
        "verify_email_token": dbVerify.token
    }
    return res.success()


@csrf_exempt
@load_json
def signup(request):
    """
        @description: This function handles the signup request
    """
    res = Response()
    formResp = profile_forms.SignupUserForm(request.POST)
    if not formResp.is_valid():
        return res.form_error(formResp)
    
    cleaned_data = formResp.cleaned_data

    # todo: Check if user is connected.
    if request.user.is_authenticated:
        dbProfile = profile_models.Profile.objects.get(user=request.user)
        if dbProfile.is_anonymous:
            return signup_anonymous_profile(dbProfile, cleaned_data)
        return res.error("You are already connected.")
    
    # todo: Observe if the user is 

    dbUser = profile_models.User.objects.create_user(
        username=cleaned_data['username'],
        email=cleaned_data['email'],
        password=cleaned_data['password'],
        first_name=cleaned_data['first_name'],
        last_name=cleaned_data['last_name'],
    )
    dbUser.save()
    dbProfile = profile_models.Profile(
        user=dbUser,
    )
    dbProfile.save()
    
    dbVerify = profile_libs.generate_verify_token(dbProfile)
    profile_libs.send_verify_token_with_email(dbVerify)

    res.DEV = {
        "verify_email_token": dbVerify.token
    }
    return res.success()