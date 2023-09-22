from kernel.http import Response
from profiles.forms import ResetPasswordVerifyTokenForm
from django.views.decorators.csrf import csrf_exempt
from kernel.http.decorators import load_json

@csrf_exempt
@load_json
def reset_password_verify_token(request):
    """
        @description: This function handles the reset password request
    """
    res = Response()
    form = ResetPasswordVerifyTokenForm(request.POST)

    if not form.is_valid():
        return res.form_error(form)
    
    return res.success()