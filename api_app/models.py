from django.db import models
from django_countries.fields import CountryField


class Address(models.Model):
    """create model for addresses"""

    company_name = models.CharField(max_length=50, null=False, blank=False)
    location_name = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address = models.CharField(max_length=80, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        """ Rendering the names in the database"""
        return str(self.location_name)
