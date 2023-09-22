from kernel.http import Response
from kernel.http.decorators import load_json
from django.views.decorators.csrf import csrf_exempt
from profiles.forms import ResetPasswordVerifyTokenForm, ResetPasswordForm

@csrf_exempt
@load_json
def reset_password(request):
    """
        @description: This function handles the reset password request
    """
    res = Response()
    tokenForm = ResetPasswordVerifyTokenForm(request.POST)
    if not tokenForm.is_valid():
        return res.form_error(tokenForm)
    
    passwordForm = ResetPasswordForm(request.POST)
    if not passwordForm.is_valid():
        return res.form_error(passwordForm)
    
    dbToken = tokenForm.cleaned_data.get('token')
    password = passwordForm.cleaned_data.get('password')

    dbToken.profile.user.set_password(password)
    dbToken.status = 'USED'
    dbToken.save()

    return res.success()