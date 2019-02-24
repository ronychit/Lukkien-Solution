from django import forms
from .models import Customer,Shipping
from .validators import validate_phonenumber
from bootstrap_datepicker_plus import DatePickerInput
import datetime

class CustomerForm(forms.ModelForm):
    """Form Class for Customer Model"""
    phone_number = forms.CharField(required=True,validators=[validate_phonenumber],widget= forms.TextInput(attrs={'placeholder':'+31 0123456789'}))
    DOB = forms.DateField(required=True,label='Date Of Birth',widget=DatePickerInput(options={"format": "YYYY-MM-DD",'maxDate': str(datetime.date.today())}))
    class Meta:
        model = Customer
        fields = "__all__"


class ShippingForm(CustomerForm):
    """Form Class for Shipping Model"""
    DOB = None
    class Meta:
        model = Shipping
        fields = "__all__"

