from django.contrib.auth.forms import UserCreationForm
from django import forms
from company import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import re

phone_re = re.compile(r'^[\d]{10}$')
phone_validator = RegexValidator(regex=phone_re, message='Invalid phone number')


class CompanyDataForm(forms.ModelForm):
    your_name = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Your Name'}), label="Name")
    your_postion = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Your Position'}), label="Postion")
    name_of_founders = forms.CharField(max_length=1000, widget=forms.TextInput(attrs = { 'class': 'input100', 'placeholder': 'Eg:- Elon Musk'}), label="Name of the founder(s)")
    description = forms.CharField(widget=forms.Textarea(attrs = { 'class': 'input100','placeholder':'Brief description of your startup'}), label="Brief Description")
    others = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Others Profiles (if any)'}), label='Other Profiles', required=False)
    number_of_vacancies = forms.IntegerField(widget=forms.NumberInput(attrs = { 'class': 'input100','placeholder':'Eg - 10, 8 etc'}))
    location = forms.CharField(max_length=100, widget=forms.TextInput(attrs = { 'class': 'input100', 'placeholder': 'Eg - Work From Home, Bangalore etc'}), label="Location")
    stipend_offered = forms.CharField(widget=forms.NumberInput(attrs = { 'class': 'input100','placeholder':'10000'}), label="Stipend Offered(in INR)")
    work_profile_description = forms.CharField(widget=forms.Textarea(attrs = { 'class': 'input100','placeholder':''}), label="Brief description of the work profile of internship")
    other_incentive = forms.CharField(widget=forms.Textarea(attrs = { 'class': 'input100','placeholder':'Accomodation, Travel etc'}), label="Any other incentives")
    requirements = forms.CharField(widget=forms.Textarea(attrs = { 'class': 'input100','placeholder':''}), label="Any specific requirements")
    reference = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Eg:- Social Media, Website etc'}), label="How did you come to know about us?")
    
    class Meta:
        model = models.CompanyData
        fields = [
            'your_name',
            'your_postion',
            'name_of_founders',
            'description',
            'profiles_offered',
            'others',
            'number_of_vacancies',
            'location',
            'stipend_offered',
            'work_profile_description',
            'other_incentive',
            'requirements',
            'reference'
        ]

