from gpm.http import Response
from gpm.http.decorators import load_json
from django.views.decorators.csrf import csrf_exempt
from profiles.forms import VerifyIdentifierForm


@csrf_exempt
@load_json
def verify_email(request):
    """
        @description: This function handles the verify email request
    """
    res = Response()
    form = VerifyIdentifierForm(request.POST)
    if not form.is_valid():
        return res.form_error(form)
    
    token = form.cleaned_data.get('token')
    token.profile.email_verified = True
    token.profile.save()

    token.status = 'USED'
    token.save()
    
    return res.success()