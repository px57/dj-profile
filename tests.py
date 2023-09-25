from django.test import TestCase

from django.test import TestCase

from kernel.http.request import FakeRequest

from profiles.models import Profile

from uuid import uuid4
from django.test import Client
from profiles.libs import password_generator


def createBasicProfile(**kwargs):
    """
        @description: Créer un profile avec les arguments dans la variables kwargs.
        @description: puis ont réalise un connections.
    """
    requiredParams = ['group']
    c = Client()
    email = uuid4().hex[0:22] + '@yopmail.com'
    password = password_generator()
    response = c.post('/v1/auth/signup/', {
          'username': uuid4().hex,
          'firstname': uuid4().hex[0:18],
          'lastname': uuid4().hex[0:18],
          'email': email,

          'password': password,
          'confirmPassword': uuid4().hex,

          'birthdate': '03/05/1992',
          'phone_number': '',
          'group': kwargs.get('group', 'root'),
          'referalCode': ''
        },
        HTTP_ACCEPT_LANGUAGE='fr'
    )
    dbProfile = Profile.objects.filter(user__email=email).first()
    if dbProfile is None:
        raise Exception('createBasicProfile: dbProfile is None')
    dbProfile.httpClient = c

    # *** Signin ***
    response = dbProfile.httpClient.post('/v1/auth/signin/', {
      'identifier': email,
      'password': password,
    })

    return dbProfile
