from kernel.http.decorators import load_json
from kernel.http import Response
from kernel.http import load_response 
from kernel.message.centralize import switcher_send_message

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from profiles.models import ResetPasswordModels, Profile
from profiles.forms import ForgotPasswordForm

from token_manager.libs import create_token
from token_manager.rules.stack import TOKEN_MANAGER_RULESTACK

from profiles.__interface__.token_manager import TokenForgetPasswordRule
from profiles.__interface__.mailling import MailForgetPassword
from profiles.rules.stack import PROFILES_RULESTACK

from uuid import uuid4


def defineResetPasswordSessionValue(
        request, 
        dbProfile, 
        dBresetPasswordModels
    ):
    """
    Définir la sessions lors de la demande de mise à jours.

    Args:
        request: La requête
        dbProfile: Le profile
        dBresetPasswordModels: Le model de reset password
    """
    serializedProfile = dbProfile.serialize(request)

    request.session['resetPassword__dbprofile'] = {
        'dbProfile': serializedProfile,
        'dbProfile': {
            'id': serializedProfile['id']
        },
        'dbDigitCode': dBresetPasswordModels.serialize(request),
        'digitCodeEntried': False,
    };

@csrf_exempt
@load_json
@load_response(stack=PROFILES_RULESTACK)
def forget_password(
        request, 
        res=None
    ):
    """
    This function handles the forget password request

    Args:
        request: The request object
        res: The response object
    """
    form = ForgotPasswordForm(request.POST)

    if not form.is_valid():
        return res.form_error(form)
    
    dbProfile: Profile = form.cleaned_data.get('email')
    dbToken = create_token(
        TOKEN_MANAGER_RULESTACK.get_rule(TokenForgetPasswordRule),
        relatedModelId=dbProfile.id
    )
    
    switcher_send_message(
        _inSwitch=MailForgetPassword,
        res=res,
        sendTo=dbProfile,
        sendBy=dbProfile,
        params={
            'VERIFY_URL_TOKEN': dbToken.create_redirect_url(res),
            'dbProfile': dbProfile
        }
    )

    return res.success()