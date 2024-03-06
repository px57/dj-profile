
from category.__rules__.stack import CATEGORY_RULESTACK
from category.__rules__.default_category import DefaultRuleClass

class DefaultRuleClass(DefaultRuleClass):
    """
    The default rule class. 
    """

    label = 'PROFILE:CATEGORY'


CATEGORY_RULESTACK.set_rule(DefaultRuleClass)