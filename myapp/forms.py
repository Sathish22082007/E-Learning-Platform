from django import forms
from .models import Customer  # Make sure you have a Customer model in models.py

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email']
