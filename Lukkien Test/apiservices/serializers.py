from rest_framework import serializers
from customer.models import Customer,Shipping

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer class for Customer Model Data"""
    class Meta:
        model = Customer
        fields = "__all__"

class ShippingSerializer(serializers.ModelSerializer):
    """Serializer class for Customer Model Data"""
    class Meta:
        model = Shipping
        fields = "__all__"