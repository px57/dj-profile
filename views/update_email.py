

from gpm.http.decorators import load_response

from profiles.rules.stack import PROFILES_RULESTACK
from profiles.forms import UpdateEmailForm
from profiles.decorators import load_profile

from django.views.decorators.csrf import csrf_exempt

@load_profile
@load_response(
    stack=PROFILES_RULESTACK,
    json=True,
    form=UpdateEmailForm,
)
def update_email(request, res=None):
    """
    Update the email of the user.
    """
    _in = res.get_interface()
    
    print (request.profile)

    return res.success()