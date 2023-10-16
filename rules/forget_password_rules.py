
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
            self,
            res: Response, 
            dbProfile: Profile, 
            dbToken: TokenModels):
        """
            @desription: Get the params to generate the email. 
        """
        return {
            'email': dbProfile.user.email,
            'token': dbToken.token,
            'url': self.frgpassword__email__url(res, dbProfile, dbToken)
        }

    def frgpassword__email__url(
            self,
            res: Response, 
            dbProfile: Profile, 
            dbToken: TokenModels):
        """
            @description: Get the url to generate the email. 
        """
        return dbToken.create_redirect_url(res)

FORGET_PASSWORD_RULESTACK = RulesStack()
FORGET_PASSWORD_RULESTACK.set_rule(ForgetPasswordDefaultRule())