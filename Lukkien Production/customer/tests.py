from django.test import TestCase
from .forms import *   # import all forms
from datetime import datetime
from django.urls import reverse_lazy

class Customer_Form_Test(TestCase):
    """Unit Test Class for Customer Form"""
    def test_CustomerForm_valid(self):
        """Unit test for Customer Form with Valid Data"""
        form = CustomerForm(data={'first_name': "Jack",'last_name':"Bown",'phone_number':"+91 1231231234",'email':"user@mp.com", 'DOB':datetime.strptime("2015-04-03",'%Y-%m-%d').date()})
        self.assertTrue(form.is_valid())

    def test_CustomerForm_invalid(self):
        """Unit test for Customer Form with Invalid Data - Phone number is Invalid"""
        form = CustomerForm(data={'first_name': "Jack", 'last_name': "Bown", 'phone_number': "1231231234", 'email': "user@mp.com",'DOB': datetime.strptime("2015-04-03", '%Y-%m-%d').date()})
        self.assertFalse(form.is_valid())

class Shipping_Form_Test(TestCase):
    """Unit Test Class for Shipping Form"""
    def test_ShippingForm_valid(self):
        """Unit test for Customer Form with Valid Data"""
        form = ShippingForm(data={'first_name': "Jack",'last_name':"Bown",'phone_number':"+91 1231231234",'email':"user@mp.com",'postal_code':"123",'city':"abcd",'street':"ad33",'house_number':"22D"})
        self.assertTrue(form.is_valid())

    def test_ShippingForm_invalid(self):
        """Unit test for Customer Form with Invalid Data - Email is Invalid"""
        form = ShippingForm(data={'first_name': "Jack", 'last_name': "Bown", 'phone_number': "+91 1231231234", 'email': "mghj",'postal_code': "123", 'city': "abcd", 'street': "ad33", 'house_number': "22D"})
        self.assertFalse(form.is_valid())


class Views_Test(TestCase):
    """Unit Test Class for Customer and Shipping create views"""
    def test_create_customer_validform_view(self):
        """Unit test for Customer create view with Valid Data"""
        response = self.client.post(reverse_lazy('customer_create'),{'first_name': "Jack", 'last_name': "Bown", 'phone_number': "+91 2312312341",'email': "user@mp.com",'DOB': datetime.strptime("2015-04-03", '%Y-%m-%d').date()})
        self.assertEquals(response.status_code,302)

    def test_create_customer_invalidform_view(self):
        """Unit test for Customer create view with Invalid Data - Phone number is Invalid"""
        response = self.client.post(reverse_lazy('customer_create'),{'first_name': "Jack", 'last_name': "Bown", 'phone_number': "2312312341",'email': "user@mp.com",'DOB': datetime.strptime("2015-04-03", '%Y-%m-%d').date()})
        self.assertEquals(response.status_code,200)

    def test_create_shipping_validform_view(self):
        """Unit test for Customer create view with Valid Data"""
        response = self.client.post(reverse_lazy('shipping_create'),{'first_name': "Jack",'last_name':"Bown",'phone_number':"+91 1231231234",'email':"user@mp.com",'postal_code':"123",'city':"abcd",'street':"ad33",'house_number':"22D"})
        self.assertEquals(response.status_code,302)

    def test_create_shipping_invalidform_view(self):
        """Unit test for Customer create view with Invalid Data - Email is Invalid"""
        response = self.client.post(reverse_lazy('shipping_create'),{'first_name': "Jack", 'last_name': "Bown", 'phone_number': "+91 1231231234", 'email': "mghj",'postal_code': "123", 'city': "abcd", 'street': "ad33", 'house_number': "22D"})
        self.assertEquals(response.status_code,200)
