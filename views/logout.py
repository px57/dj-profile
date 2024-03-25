from django.contrib.auth import logout as django_logout
from gpm.http import Response



def logout(request):
    """Easy logout."""
    res = Response()
    django_logout(request)
    return res.success()
