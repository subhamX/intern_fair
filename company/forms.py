from django.contrib.auth.forms import UserCreationForm
from django import forms
from company import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import re

phone_re = re.compile(r'^[\d]{10}$')
phone_validator = RegexValidator(regex=phone_re, message='Invalid phone number')

    # )
    # address = models.CharField(max_length=1000, null=True)
    # your_name = models.CharField(max_length=100, null=True)
    # your_postion = models.CharField(max_length=100, null=True)
    # description = models.CharField(max_length=1000, null=True)
    # profiles_offered
class CompanyDataForm(forms.ModelForm):
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs = { 'class': 'input100', 'placeholder': 'Address'}))
    your_name = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Your Name'}))
    your_postion = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Your Position'}))
    description = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Brief description of your startup'}))
    others = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Others Profiles (if any)'}), label='Other Profiles', required=False)
    contact_number = forms.IntegerField(widget=forms.NumberInput(attrs = { 'class': 'input100','placeholder':'Contact Number'}), validators= [phone_validator] )
    
    class Meta:
        model = models.CompanyData
        fields = [
            'your_name',
            'address',
            'your_postion',
            'description',
            'profiles_offered',
            'others',
            'contact_number'
        ]

