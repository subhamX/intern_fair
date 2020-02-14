from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import re

phone_re = re.compile(r'^\d{10}$')
entry_number_re = re.compile(r'^2\d\d\d\w\w\w\d\d\d\d$')
iitrpr_email_re = re.compile(r'^[\w]+@iitrpr.ac.in$')
phone_validator = RegexValidator(regex=phone_re, message='Invalid Phone Number')
entry_number_validator = RegexValidator(regex=entry_number_re, message='Invalid Entry Number')
iitrpr_email_validator = RegexValidator(regex=iitrpr_email_re, message='Email provider should be IIT Ropar')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=40, widget=forms.TextInput(attrs = { 'class': 'input100', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs = { 'class': 'input100', 'placeholder': 'Password'}))


class CompanySignUpForm(forms.ModelForm):
    company_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs = { 'class': 'input100', 'placeholder': 'Company Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Email-ID'}))
    contact_number = forms.CharField(widget=forms.NumberInput(attrs = { 'class': 'input100','placeholder':'Contact Number'}), validators= [phone_validator] )
    website_link = forms.URLField(widget=forms.URLInput(attrs = { 'class': 'input100','placeholder':'Link'}), initial='http://')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100' ,'placeholder':'Password'
        }), min_length=8)
    class Meta:
        model = models.CompanyProfile
        fields = [
            'company_name',
            'email',
            'contact_number',
            'website_link',
        ]



class StudentSignUpForm(forms.ModelForm):
    CHOICES = (
        (1, '1st Year'),
        (2, '2nd Year'),
        (3, '3rd Year'),
        (4, '4th Year'),
    )
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'input100','placeholder':'Name'}))
    entry_number=forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Entry Number'}), validators=[entry_number_validator])
    email = forms.EmailField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Email'}), validators=[iitrpr_email_validator])
    contact_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'input100','placeholder':'Contact Number'}), validators= [phone_validator] )
    college_year=forms.ChoiceField(widget=forms.Select(attrs={'class':'input100','placeholder':'Year'}),choices=CHOICES )
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

        
class UploadCVForm(forms.ModelForm):
    cv = forms.FileField(label="Upload CV")
    class Meta:
        model = models.StudentProfile
        fields = [
            'cv',
        ]