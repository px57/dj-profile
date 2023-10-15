
from token_manager.rules.stack import TOKEN_MANAGER_RULESTACK
from token_manager.rules.defaul_rule_class import DefaultRuleClass

class ForgetPasswordTokenManager(DefaultRuleClass):
    """
        @description: This class is the avatar file rule
    """

    @property
    def label(self):
        return 'forget_password'

    token_expiration_allow = True

TOKEN_MANAGER_RULESTACK.set_rule(ForgetPasswordTokenManager())