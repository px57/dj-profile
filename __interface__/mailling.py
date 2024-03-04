
from mailling.rules.stack import MAILLING_RULESTACK
from mailling.rules.default_mailling import DefaultRuleClass

class MailVerifyProfile(DefaultRuleClass):
    """
    This rule is used to send an email
    """
    label = 'PROFILE:VERIFY_PROFILE'
    unsubscribe_enable = False


class MailForgetPassword(DefaultRuleClass):
    """
    This rule is used to send an email
    """
    label = 'PROFILE:FORGET_PASSWORD'

    unsubscribe_enable = False

MAILLING_RULESTACK.add_rule(MailVerifyProfile)
MAILLING_RULESTACK.add_rule(MailForgetPassword)