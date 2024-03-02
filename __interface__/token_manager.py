

from token_manager.rules.defaul_rule_class import DefaultRuleClass
from token_manager.rules.stack import TOKEN_MANAGER_RULESTACK

class VerifyTokenRule(DefaultRuleClass):
    """
    This rule is used to verify a token
    """

    label = "VERIFY_PROFILE_TOKEN"

class ForgetPasswordRule(DefaultRuleClass):
    """
    This rule is used to verify a token
    """

    label = "FORGET_PASSWORD"

    """
    The token expiration allow.
    """
    token_expiration_allow = True

    """
    The token 
    """
    token_max_size = 128

TOKEN_MANAGER_RULESTACK.add_rule(ForgetPasswordRule)
TOKEN_MANAGER_RULESTACK.add_rule(VerifyTokenRule)