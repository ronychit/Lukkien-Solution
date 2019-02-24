from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CustomerForm,ShippingForm
from django.urls import reverse_lazy


class CustomerCreateView(SuccessMessageMixin,CreateView):
    """View to save details of Customer"""
    template_name = 'customer.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customer_create')
    success_message = 'Customer Details Saved Successfully'

class ShippingCreateView(SuccessMessageMixin,CreateView):
    """View to save details of Shipping"""
    template_name = 'shipping.html'
    form_class = ShippingForm
    success_url = reverse_lazy('shipping_create')
    success_message = 'Shipping Details Saved Successfully'