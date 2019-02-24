from django.db import models

class CommonDetails(models.Model):
    """Abstract class for Customer and Shipping Models"""
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    class Meta:
        abstract = True

class Customer(CommonDetails):
    """Model Class for Customer"""
    DOB = models.DateField(blank=False,null=False)

class Shipping(CommonDetails):
    """Model Class for Shipping"""
    postal_code = models.CharField(max_length=10,blank=False,null=False)
    city= models.CharField(max_length=20,blank=False,null=False)
    street = models.CharField(max_length=20,blank=False,null=False)
    house_number = models.CharField(max_length=20,blank=False,null=False)


