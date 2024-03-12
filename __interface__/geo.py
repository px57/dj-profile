
from geo.rules.stack import GEO_RULESTACK
from geo.rules.default_geo import DefaultRuleClass

class SelectCountry(DefaultRuleClass):
    """
    This rule is used to select the country.
    """
    label = 'PROFILE:GEO'

GEO_RULESTACK.add_rule(SelectCountry)