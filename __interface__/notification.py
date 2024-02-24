

from notification.rules.stack import NOTIFICATION_RULESTACK
from notification.rules.default_notification import DefaultRuleClass

class Notification(DefaultRuleClass):
    """
    The default rule class. 
    """

    label = 'WELCOME'

    allow = True