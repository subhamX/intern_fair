from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts import models
from django.contrib.auth.models import User

# class SignUpForm(UserCreationForm):
#     password1 = forms.CharField(
#         label='Password:', 
#         widget=forms.PasswordInput(attrs={
#         })
#     )
#     password2 = forms.CharField(
#         label='Password Confirmation:', 
#         widget=forms.PasswordInput(attrs={
#         })
#     )
#     username = forms.CharField(
#         label='Username:',
#         widget=forms.TextInput(attrs={
#             'autofocus': None
#         })
#     )
#     first_name = forms.CharField(
#         label='First Name:',
#         widget=forms.TextInput(attrs={
#             'autofocus': 'autofocus'
#         })
#     )
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             # 'contact_number'
#         ]

# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=40)
#     password = forms.CharField(widget=forms.PasswordInput())


class CompanySignUpForm(forms.ModelForm):
    company_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs = { 'class': 'input100', 'placeholder': 'Comapny Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Email-ID'}))
    contact_number = forms.IntegerField(widget=forms.NumberInput(attrs = { 'class': 'input100','placeholder':'Contact Number'}))
    website_link = forms.SlugField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Link'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'input100' ,'placeholder':'Password'
        }))
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
    entry_number=forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class':'input100','placeholder':'Entry Number'}))
    email = forms.EmailField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Email'}))
    contact_number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'input100','placeholder':'Contact Number'}))
    college_year=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'input100','placeholder':'Year'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
         'class': 'input100' ,'placeholder':'Password'
        }))
    class Meta:
        model = models.StudentProfile
        fields = [
            'name',
            'entry_number',
            'email',
            'contact_number',
            'college_year'
        ]

        