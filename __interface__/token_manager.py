

from token_manager.rules.defaul_rule_class import DefaultRuleClass
from token_manager.rules.stack import TOKEN_MANAGER_RULESTACK

class TokenVerifyProfileRule(DefaultRuleClass):
    """
    This rule is used to verify a token
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

TOKEN_MANAGER_RULESTACK.add_rule(TokenForgetPasswordRule)
TOKEN_MANAGER_RULESTACK.add_rule(TokenVerifyProfileRule)