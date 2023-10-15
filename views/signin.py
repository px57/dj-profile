from kernel.http import Response
from kernel.http.decorators import load_json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from profiles.models import Profile
from django.contrib.auth import authenticate, login, logout
import re


@csrf_exempt
@load_json
def signin(request):
    """
        @description: This function handles the signin request
    """
    res = Response()
    form_error = {
        '__signin__': ['not_exists']
    }
    
    identifier = request.POST.get('identifier')
    password = request.POST.get('password')
    is_email_tentative_login = re.match(r"[^@]+@[^@]+\.[^@]+", identifier)

    if is_email_tentative_login:
        dbUser = User.objects.filter(email=identifier).first()
    else:
        dbUser = User.objects.filter(username=identifier).first()

    if not dbUser:
        res.form_error = form_error
        return res.error('user not exists')

    try: 
        dbProfile = Profile.objects.get(user=dbUser)
    except Profile.DoesNotExist:
        res.form_error = {
            '__signin__': ['profile_dont_exists']
        }
        return res.error('profile_dont_exists')

    user = authenticate(username=dbUser.username, password=password)
    if user is None:
        res.form_error = form_error
        return res.error('after_user_authenticate')

    login(request, user)
    return res.success()
