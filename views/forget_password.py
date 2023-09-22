from kernel.http.decorators import load_json
from django.views.decorators.csrf import csrf_exempt
from kernel.http.decorators import load_json
from kernel.http import Response
from django.views.decorators.csrf import csrf_exempt
from profiles.models import ResetPasswordModels, Profile
from profiles.forms import ForgotPasswordForm
from django.conf import settings

from uuid import uuid4
import json


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
def forget_password(request):
    """
        @description: This function handles the forget password request
    """
    res = Response()
    form = ForgotPasswordForm(request.POST)
    if not form.is_valid():
        return res.form_error(form)
    
    dbProfile = form.cleaned_data.get('email')
    dBresetPasswordModels = ResetPasswordModels(
        profile=dbProfile,
        token=uuid4().hex,
    )
    dBresetPasswordModels.save()
    defineResetPasswordSessionValue(request, dbProfile, dBresetPasswordModels)


    res.DEV = {
        'digitCode': dBresetPasswordModels.token,
    }

        # CommunicationManager(request, dbProfile).FORGOT_PASSWORD(
        #     FIRSTNAME=dbProfile.firstname,
        #     CODE_VERIF=dBresetPasswordModels.token,
        #     MAIL_USER=dbProfile.email,
        # )
    return res.success()