from rest_framework import viewsets
from customer.models import Customer,Shipping
from . import serializers

class CustomerViewSet(viewsets.ModelViewSet):
    """API for Customer endpoint"""
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

class ShippingViewSet(viewsets.ModelViewSet):
    """API for Shipping endpoint"""
    queryset = Shipping.objects.all()
    serializer_class = serializers.ShippingSerializer
