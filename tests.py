from django.test import TestCase
from django.urls import reverse

from kernel.http.request import FakeRequest

from profiles.models import Profile

from uuid import uuid4
from django.test import Client
from profiles.libs import password_generator

from token_manager.models import TokenModels


def createBasicProfile(**kwargs) -> Profile:
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


class SignupTest(TestCase):
    """
    Signup test.
    """
  


class ForgetPasswordTest(TestCase):
    """
      @description: 
    """

    def test_all_process_to_change_password(self):
        """
          @description: 
        """
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>> [FORGET PASSWORD] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        dbProfile = createBasicProfile(group='root')
        c = Client()
        response = c.post(reverse('profiles__forget_password'), {
            'email': dbProfile.user.email
        })
        try: 
          self.assertEqual(response.json()['success'], True)
        except:
            self.fail('forget password failed')
        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [VERIFY TOKEN] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # -> Verify token has been created.
        dbToken = TokenModels.objects.first()
        self.assertNotEqual(dbToken, None)

        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [END] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        #>>>>>>>>>>>>>>>>>>>>>>>>>>>>> [RESET PASSWORD] <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        # -> Verify change the password.
        pathname = reverse('profiles__reset_password')
        c = Client()

        new_password = password_generator()
        response = c.post(pathname, {
            'interface_name': 'default',
            'token': dbToken.token,
            'password': new_password,
            'confirm_password': new_password
        })
        try: 
          self.assertEqual(response.json()['success'], True)
        except:
            self.fail('reset password failed')