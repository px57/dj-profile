from kernel.http.decorators import load_json
from kernel.http import Response
from kernel.interfaces.decorators import load_interface

from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from profiles.models import ResetPasswordModels, Profile
from profiles.forms import ForgotPasswordForm
from profiles.rules.forget_password_rules import FORGET_PASSWORD_RULESTACK
from profiles.emails import ProfileEmails

from token_manager.libs import create_token, find_token
from token_manager.models import TokenModels

from uuid import uuid4


def defineResetPasswordSessionValue(request, dbProfile, dBresetPasswordModels):
    """
        @description: Définir la sessions lors de la demande de mise à jours.
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
@load_interface(FORGET_PASSWORD_RULESTACK)
def forget_password(request):
    """
        @description: This function handles the forget password request
    """
    res = Response(request=request)
    form = ForgotPasswordForm(request.POST)

    if not form.is_valid():
        return res.form_error(form)
    
    dbProfile: Profile = form.cleaned_data.get('email')
    dbToken: TokenModels = create_token(
        max_size=32,
        relatedModel='profiles.Profile',
        relatedModelId=dbProfile.id
    )

    ProfileEmails().FORGET_PASSWORD(res, dbProfile, dbToken)
    return res.success()