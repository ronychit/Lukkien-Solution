from django.core.exceptions import ValidationError
import  re

def validate_phonenumber(value):
    """Function to validate phone number based on industry-standard notation specified by ITU-T E.123"""
    if not re.findall(r'^\+(?:[0-9] ?){6,14}[0-9]$',value):
        raise ValidationError('Invalid phone number',)


