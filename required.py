
from django.conf import settings

if not hasattr(settings, 'APP_NAME'):
    raise Exception('profiles.required.py :: APP_NAME is not defined in settings.py')
