
from mailling.rules.stack import MAILLING_RULESTACK
from mailling.rules.default_mailling import DefaultRuleClass

class MailVerifyProfile(DefaultRuleClass):
    """
    This rule is used to send an email
    """
    label = 'VERIFY_PROFILE'

class MailForgetPassword(DefaultRuleClass):
    """
    This rule is used to send an email
    """
    label = 'FORGET_PASSWORD'

MAILLING_RULESTACK.add_rule(MailVerifyProfile)
MAILLING_RULESTACK.add_rule(MailForgetPassword)