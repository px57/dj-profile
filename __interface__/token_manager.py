

from token_manager.rules.defaul_rule_class import DefaultRuleClass, DigitalNumericRuleClass
from token_manager.rules.stack import TOKEN_MANAGER_RULESTACK

from datetime import timedelta


class TokenVerifyProfileRule(DefaultRuleClass):
    """
    Verify the email profile with url link.
    """

    label = "PROFILE:VERIFY_PROFILE"

class TokenForgetPasswordRule(DefaultRuleClass):
    """
    This rule is used to verify a token
    """

    label = "PROFILE:FORGET_PASSWORD"

    """
    The token expiration allow.
    """
    token_expiration_allow = True

class TokenVerifyEmailRule(DigitalNumericRuleClass):
    """
    This rule is used to verify a token
    """

    label = "PROFILE:VERIFY_EMAIL"

TOKEN_MANAGER_RULESTACK.add_rule(TokenVerifyEmailRule)
TOKEN_MANAGER_RULESTACK.add_rule(TokenForgetPasswordRule)
TOKEN_MANAGER_RULESTACK.add_rule(TokenVerifyProfileRule)