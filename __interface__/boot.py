
from boot.rules.stack import BOOT_RULESTACK
from boot.rules.default_boot import DefaultRuleClass

class ProfileBoot(DefaultRuleClass):
    """
    The profile boot class.
    """

    """
    The label to identify the rule interface.
    """
    label = 'PROFILE_BOOT'

    """
    The allow flag to enable or disable the rule.
    """
    allow = True

    def __init__(self) -> None:
        super().__init__()

    def gpm_run(self, *args, **kwargs):
        """
        The run function for the boot profile.
        """
        res = kwargs.get('res', None)
        request = res.get_request()
        if not res.is_authenticated():
            return 
        res.profile = request.user.profile.serialize(request)

BOOT_RULESTACK.set_rule(ProfileBoot)