
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

    # ***************************[FIND CITY]*****************************************
    find_city_in_country = True

    @interface_load_profile
    def gpm__viewparams__find_city(self):
        """
        Get the selecteable countries.
        """
        from geo.models import CountriesRelated
        from profiles.models import Profile

        dbCountriesRelated = CountriesRelated.objects.filter(
            relatedModelId=self.request.profile.id,
            relatedModel=Profile.__module__ + '.' + Profile.__name__,
        ).first()
        return {
            'country': dbCountriesRelated.country,
        }
    
    # ***************************[SELECT CITY]*****************************************
    """
    The view of select city, is login required.
    """
    gpm__loginrequired__select_city = True

    """
    Force load the profile in the loadprofile.
    """
    gpm__loadprofile__select_city = True

    @interface_load_profile
    def gpm__viewparams__select_city(self):
        """
        Get the selecteable countries.
        """
        from geo.models import CountriesRelated
        from profiles.models import Profile

        return {
            'relatedModelId': self.request.profile.id,
            'relatedModel': Profile.__module__ + '.' + Profile.__name__,
        }

GEO_RULESTACK.add_rule(SelectCountry)