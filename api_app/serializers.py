from rest_framework import serializers
from .models import Address
from django_countries.serializers import CountryFieldMixin


class AddressSerializer(CountryFieldMixin, serializers.ModelSerializer):
    """defining model rapresentaion"""

    company_name = serializers.CharField(max_length=50)
    location_name = serializers.CharField(max_length=80, required=False)
    postcode = serializers.CharField(max_length=20)
    town_or_city = serializers.CharField(max_length=40, required=False)
    street_address = serializers.CharField(max_length=80, required=False)
    county = serializers.CharField(max_length=80)

    class Meta:
        """ model and fields to serialize"""
        model = Address
        fields = ('__all__')
