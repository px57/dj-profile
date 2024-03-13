
from geo.rules.stack import GEO_RULESTACK
from geo.rules.default_geo import DefaultRuleClass

import pycountry

class SelectCountry(DefaultRuleClass):
    """
    This rule is used to select the country.
    """
    label = 'PROFILE:GEO'

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

GEO_RULESTACK.add_rule(SelectCountry)