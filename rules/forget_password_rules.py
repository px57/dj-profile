
from kernel.interfaces.stack import RulesStack
from kernel.interfaces.interfaces import InterfaceManager
from kernel.http import Response
from profiles.models import Profile
from token_manager.models import TokenModels

class ForgetPasswordDefaultRule(InterfaceManager):
    """
        @description: 
    """

    def frgpassword__email__params(
            res: Response, 
            dbProfile: Profile, 
            dbToken: TokenModels):
        """
            @desription: Get the params to generate the email. 
        """
        params = {
            'email': dbProfile.user.email,
            'token': dbToken.token,
        }

    def frgpassword__email__url(
            res: Response, 
            dbProfile: Profile, 
            dbToken: TokenModels):
        """
            @description: Get the url to generate the email. 
        """
        return 

FORGET_PASSWORD_RULESTACK = RulesStack()
FORGET_PASSWORD_RULESTACK.set_rule(ForgetPasswordDefaultRule())