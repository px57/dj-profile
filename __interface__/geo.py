
from geo.rules.stack import GEO_RULESTACK
from geo.rules.default_geo import DefaultRuleClass

from profiles.decorators import interface_load_profile

import pycountry

class SelectCountry(DefaultRuleClass):
    """
    This rule is used to select the country.
    """
    label = 'PROFILE:GEO'

    """
    The selecteable countries code list.
    """
    selecteable_countries_code_list = [
        # united states
        'US',
        # united kingdom
        'GB',
        # france
        'FR',
        # United Arab Emirates
        'AE',
    ]

    @interface_load_profile
    def gpm__viewparams__select_country(self):
        """
        Get the selecteable countries.
        """
        from profiles.models import Profile

        return {
            'relatedModelId': self.request.profile.id,
            'relatedModel': Profile.__module__ + '.' + Profile.__name__,
        }

GEO_RULESTACK.add_rule(SelectCountry)