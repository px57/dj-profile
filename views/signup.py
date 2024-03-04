from kernel.http import Response
from kernel.http.decorators import load_json
from kernel.http import load_response

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from profiles import forms as profile_forms
from profiles import models as profile_models
from profiles import libs as profile_libs

from profiles.rules.stack import PROFILES_RULESTACK
from profiles.__interface__.token_manager import TokenVerifyProfileRule  
from profiles.__interface__.mailling import MailVerifyProfile

from token_manager.rules.stack import TOKEN_MANAGER_RULESTACK
from token_manager.libs import create_token

from kernel.message.centralize import switcher_send_message

def signup_anonymous_profile(
        dbProfile, 
        cleaned_data,
        res=None
    ):
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
@load_response(stack=PROFILES_RULESTACK)
def signup(request, res=None):
    """
        @description: This function handles the signup request
    """
    _in = res.get_interface()
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
    
    dbToken = create_token(
        TOKEN_MANAGER_RULESTACK.get_rule(TokenVerifyProfileRule),
        relatedModelId=dbProfile.id
    )

    switcher_send_message(
        _inSwitch=MailVerifyProfile,
        res=res,
        sendTo=dbProfile,
        sendBy=dbProfile,
        params={
            'VERIFY_URL_TOKEN': dbToken.create_redirect_url(res)
        }
    )

    res.profile = dbProfile.serialize(request)

    res.DEV = {
        "verify_email_token": dbToken.create_redirect_url(res)
    }
    return res.success()
