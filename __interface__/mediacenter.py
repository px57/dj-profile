
from mediacenter.rules.stack import MEDIACENTER_RULESTACK
from mediacenter.rules.defaul_rule_class import DefaultRuleClass

class AvatarFileRule(DefaultRuleClass):
    """
        @description: This class is the avatar file rule
    """

    autocrop_allow = True

    @property
    def label(self):
        return 'avatar'
    
    def event_after_upload(self, request, instance):
        request.profile.avatar = instance
        request.profile.save()
        return super().event_after_upload(request, instance)

MEDIACENTER_RULESTACK.set_rule(AvatarFileRule)