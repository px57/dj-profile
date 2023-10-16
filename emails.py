
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
        # print (res.get_interface().email_forget_password_params(res, dbProfile, dbToken))
        params = res.get_interface().frgpassword__email__params(res, dbProfile, dbToken)
        print (params)

    def WELCOME(self, dbProfile: Profile):
        """
            @description:
            @param.dbProfile -> Profile
        """
