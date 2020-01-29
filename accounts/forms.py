from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import re

phone_re = re.compile(r'^[\d]{10}$')
entry_number_re = re.compile(r'^2\d\d\d\w\w\w\d\d\d\d$')
iitrpr_email_re = re.compile(r'^[\w]+@iitrpr.ac.in$')
phone_validator = RegexValidator(regex=phone_re, message='Invalid phone number')
entry_number_validator = RegexValidator(regex=entry_number_re, message='Invalid entry number')
iitrpr_email_validator = RegexValidator(regex=iitrpr_email_re, message='Email provider should be IITRPR')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs = { 'class': 'input100', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = { 'class': 'input100', 'placeholder': 'Password'}))


class CompanySignUpForm(forms.ModelForm):
    company_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs = { 'class': 'input100', 'placeholder': 'Company Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Email-ID'}))
    contact_number = forms.IntegerField(widget=forms.NumberInput(attrs = { 'class': 'input100','placeholder':'Contact Number'}), validators= [phone_validator] )
    website_link = forms.URLField(widget=forms.URLInput(attrs = { 'class': 'input100','placeholder':'Link'}), initial='http://')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100' ,'placeholder':'Password'
        }), min_length=8)
    class Meta:
        model = models.CompanyProfile
        fields = [
            'email',
            'company_name',
            'website_link',
            'contact_number',
        ]



class StudentSignUpForm(forms.ModelForm):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'input100','placeholder':'Name'}))
    entry_number=forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Entry Number'}), validators=[entry_number_validator])
    email = forms.EmailField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Email'}), validators=[iitrpr_email_validator])
    contact_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'input100','placeholder':'Contact Number'}), validators= [phone_validator] )
    college_year=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'input100','placeholder':'Year'}), )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
         'class': 'input100' ,'placeholder':'Password'
        }), min_length=8)
    class Meta:
        model = models.StudentProfile
        fields = [
            'name',
            'entry_number',
            'email',
            'contact_number',
            'college_year'
        ]

        