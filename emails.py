
from profiles.models import Profile
from token_manager.models import TokenModels
from kernel.http import Response

class ProfileEmails(object):
    """
        @description: 
    """
    
    def FORGET_PASSWORD(self,
        res: Response,
        dbProfile: Profile, 
        dbToken: TokenModels
    ):
        """
            @description:
            @param.dbProfile -> Profile
            @param.dbToken -> Token 
        """
        params = res.get_interface().frgpassword__email__params(res, dbProfile, dbToken)
        print ('################################')
        print (params)
        # TODO: Send the email.

    def WELCOME(self, dbProfile: Profile):
        """
            @description:
            @param.dbProfile -> Profile
        """
