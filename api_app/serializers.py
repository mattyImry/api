from rest_framework import serializers
from .models import Address
from django_countries.serializers import CountryFieldMixin


class AddressSerializer(CountryFieldMixin, serializers.ModelSerializer):
    """defining model rapresentaion for JSON format"""

    company_name = serializers.CharField(max_length=50, required=False)
    town_or_city = serializers.CharField(max_length=40, required=False)
    street_address = serializers.CharField(max_length=80, required=False)

    class Meta:
        model = Address()
        fields = ('__all__')
