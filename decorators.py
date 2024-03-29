
# from django.conf import settings
# from django.http import JsonResponse
# from django.contrib.auth.models import User

# from d
from django.conf import settings
from functools import wraps

import jwt

def load_profile_when_im_authenticated(request):
    """
        @description: 
        @param.request: 
    """
    from profiles.models import Profile
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
    from gpm.http import Response

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
    from django.conf import settings
    from django.http import JsonResponse
    from functools import wraps


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

def interface_load_profile(__class):
    """
    Charge le profile à l'intérieurs des éléments.
    """
    def wrap(self, *args, **kwargs):
        load_profile_when_im_authenticated(self.request)
        return __class(self, *args, **kwargs)
    
    wrap.__doc__ = __class.__doc__
    wrap.__name__ = __class.__name__
    return wrap

