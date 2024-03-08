
from category.__rules__.stack import CATEGORY_RULESTACK
from category.__rules__.default_category import DefaultRuleClass

CATEGORY_CACHE = {}

class ProfileCategoryRule(DefaultRuleClass):
    """
    The default rule class. 
    """

    label = 'PROFILE:CATEGORY'

    def relatedModel__for__set_selected_category(self):
        """
        Return the related model for the set selected category
        """
        from profiles.models import Profile
        return Profile.__module__ + '.' + Profile.__name__

    def relatedModelId__for__set_selected_category(self):
        """
        Return the related model id for the set selected category
        """
        return self.request.profile.id
    
    def relatedModelId__for__get_related_categories(self):
        """
        Return the related model id for the get related categories
        """
        return self.relatedModelId__for__set_selected_category()

    def event_set_selected_categories(self, dbSelectedCategories) -> bool:
        '''
        Set selected category is database save.
        '''
        print (dbSelectedCategories)
        return True
    

CATEGORY_RULESTACK.set_rule(ProfileCategoryRule)