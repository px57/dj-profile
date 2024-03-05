
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User

from kernel.http import Response

from profiles.models import Profile

from functools import wraps

import jwt

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

def profile_required(function):
    """
    Verifie si le profile est chargé.
    """
    def wrap(request, *args, **kwargs):
        if not request.profile:
            res = Response(request=request)
            return res.error(
                'Profile not found', 
                code=404
            )
        return function(request, *args, **kwargs)
    
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def jwt_required(f):
    @wraps(f)
    def wrap(request, *args, **kwargs):
        token = request.headers.get('Authorization', None)
        if token is None:
            return JsonResponse({'error': 'Missing token'}, status=401)
        try:
            payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
            request.user_id = payload['user_id']
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Token expired'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        return f(request, *args, **kwargs)
    return wrap