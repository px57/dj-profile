
from gpm.http import Response
from profiles.decorators import load_profile
from profiles.forms import ResetPasswordForm

@load_profile
def update_password(request):
    """
        @description: 
    """
    res = Response()
    form = ResetPasswordForm({
        'password': request.POST.get('password'),
        'confirm_password': request.POST.get('confirmPassword'),
    })
    if not form.is_valid():
        return res.form_error(form)
    request.profile.user.set_password(form.cleaned_data['password'])
    request.profile.user.save()
    return res.success()