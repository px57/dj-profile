from kernel.http import Response
from profiles import models as profile_models

def me(request):
    res = Response()
    res.is_authenticated = request.user.is_authenticated
    
    if request.user.is_authenticated:
        dbProfile = profile_models.Profile.objects.filter(user=request.user).first()
        if dbProfile.is_anonymous:
            res.is_authenticated = False

        res.profile = dbProfile.serialize(request)
    return res.success()