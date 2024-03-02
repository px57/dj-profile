

from django.utils import timezone
import os
from profiles.rules.stack import PROFILES_RULESTACK
from kernel.interfaces.interfaces import InterfaceManager
import PIL

class DefaultRuleClass(InterfaceManager):
    """
    The default rule class. 
    """

    """
    The label to identify the rule interface.
    """
    label = 'MOBILE'.upper()

    """
    The allow flag to enable or disable the rule.
    """
    description = 'Rule interface for the mobile profile'

    

PROFILES_RULESTACK.set_rule(DefaultRuleClass())