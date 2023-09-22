
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from profiles import models as profile_models
from uuid import uuid4
import json

################################################## [VERIFY-TOKEN]
def generate_verify_token(profile):
    """
        @description: This function generates the verify token
    """
    dbVerify = profile_models.VerifyIdentifier(
        profile=profile,
        token=uuid4().hex,
    )
    dbVerify.save()
    return dbVerify

def send_verify_token_with_email(dbVerify):
    """
        @description: This function verifies the token
    """


################################################## [GENERATE-ANONYMOUS-USER]
def generate_anonymous_user(request, response):
    """
        @description: This function generates the anonymous user
    """
    # -> Check if the user is already connected
    if request.user.is_authenticated:
        return

    data = {
        'username': uuid4().hex,
        'email': uuid4().hex + '@anonymous.com',
        'password': uuid4().hex,
    };
    dbUser = User(**data)
    dbUser.save()
    dbProfile = profile_models.Profile(
        user=dbUser,
        is_anonymous=True,
    )
    dbProfile.save()
    response.set_cookie('cookie_name', json.dumps(data))
    # -> Connect the user to the anonymous user
    connect_to_anonymous_user(request, response, dbUser, data)


def connect_to_anonymous_user(request, response, dbUser, data):
    """
        @description: This function connects the user to the anonymous user
    """
    user = authenticate(
        username=dbUser.username, 
        password=data['password']
    )
    login(request, dbUser)