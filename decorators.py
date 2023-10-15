
from django.contrib.auth.models import User
from kernel.http import Response
from profiles.models import Profile
import json

def load_profile_when_im_authenticated(request):
    """
        @description: 
        @param.request: 
    """
    if not request.user.is_authenticated:
        request.profile = None
        return None

    if hasattr(request, 'profile'):
        return None
    
    request.profile = Profile.objects.filter(user=request.user).first()

def load_profile(function):
    """Charge le profile à l'intérieurs des éléments."""
    def wrap(request, *args, **kwargs):
        load_profile_when_im_authenticated(request)
        return function(request, *args, **kwargs)
    
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
