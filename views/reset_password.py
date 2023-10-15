from kernel.http import Response
from kernel.http.decorators import load_json
from kernel.interfaces.decorators import load_interface

from django.views.decorators.csrf import csrf_exempt

from profiles.forms import ResetPasswordForm

from token_manager.decorators import load_token, token_required

from profiles.rules.forget_password_rules import FORGET_PASSWORD_RULESTACK

@csrf_exempt
@load_json
@load_token
@token_required
@load_interface(FORGET_PASSWORD_RULESTACK)
def reset_password(request):
    """
        @description: This function handles the reset password request
    """
    res = Response()
    dbToken = request.token
    interface = FORGET_PASSWORD_RULESTACK.get_rule(request.POST.get('interface_name'))

    passwordForm = ResetPasswordForm(request.POST)
    if not passwordForm.is_valid():
        return res.form_error(passwordForm)
    
    password = passwordForm.cleaned_data.get('password')

    # dbToken.profile.user.set_password(password)
    # dbToken.status = 'USED'
    # dbToken.save()

    return res.success()
