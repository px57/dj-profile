from kernel.http import Response
from profiles import models as profile_models
from kernel.signal import SIGNAL_CENTER

def me(request):
    res = Response(request=request)
    res.is_authenticated = request.user.is_authenticated
    
    if request.user.is_authenticated:
        dbProfile = profile_models.Profile.objects.filter(
            user=request.user
        ).first()

        if dbProfile.is_anonymous:
            res.is_authenticated = False

        res.profile = dbProfile.serialize(request)

    res.update(
        SIGNAL_CENTER.execute('profile.load_me', res)
    )
    return res.success()