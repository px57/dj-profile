
from kernel.http import Response
from profiles.decorators import load_profile
from profiles.forms import UpDateUserName

def update_email(request):
    """
        @description: 
    """
    email = request.POST.get('email')
    if request.profile.email == email:
        return False
    return True

def update_username(request):
    """
        @description:
    """
    username = request.POST.get('username')
    if request.profile.username == username:
        return False
    return True

@load_profile
def update_profile(request):
    """
        @description: 
    """
    res = Response()
    user = request.profile.user

    if update_username(request):
        usernameForm = UpDateUserName(request.POST)
        if not usernameForm.is_valid():
            return res.form_error(usernameForm)
        request.profile.user.username = usernameForm.cleaned_data.get('username')

    if update_email(request):
        pass
        # TODO: Il faut a present verifier si l'email est valide.
        # TODO: Il faut a present changer l'email de l'utilisateur.
        request.profile.user.email = request.POST.get('email')

    username = usernameForm.cleaned_data.get('username')
    # TODO: Maintenant il faut veiller a sauvegarder l'ensemble de ces donnees.
    return res.success()