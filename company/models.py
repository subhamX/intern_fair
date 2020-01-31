from django.db import models
from multiselectfield import MultiSelectField
from accounts.models import CompanyProfile
# Create your models here.


    # your_name = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Your Name'}))
    # your_postion = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Your Position'}))
    # name_of_founders = forms.CharField(max_length=1000, widget=forms.TextInput(attrs = { 'class': 'input100', 'placeholder': 'Elon Musk'}), label="Name of the founder(s)")
    # description = forms.CharField(widget=forms.Textarea(attrs = { 'class': 'input100','placeholder':'Brief description of your startup'}), label="Brief Description")
    # others = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Others Profiles (if any)'}), label='Other Profiles', required=False)
    # number_of_vacancies = forms.IntegerField(widget=forms.NumberInput(attrs = { 'class': 'input100','placeholder':'Eg - 10, 8 etc'}))
    # location = forms.CharField(max_length=100, widget=forms.TextInput(attrs = { 'class': 'input100', 'placeholder': 'Eg - Work From Home, Bangalore etc'}), label="Location")
    # stipend_offered = forms.CharField(widget=forms.NumberInput(attrs = { 'class': 'input100','placeholder':'10000'}), label="Stipend Offered(in INR)")
    # description = forms.CharField(widget=forms.Textarea(attrs = { 'class': 'input100','placeholder':''}), label="Brief description of the work profile of internship")
    # other_incentive = forms.CharField(widget=forms.Textarea(attrs = { 'class': 'input100','placeholder':'Accomodation, Travel etc'}), label="Any other incentives")
    # requirements = forms.CharField(widget=forms.Textarea(attrs = { 'class': 'input100','placeholder':''}), label="Any specific requirements")
    # reference = forms.CharField(widget=forms.TextInput(attrs = { 'class': 'input100','placeholder':'Eg:- Social Media, Website etc'}), label="How did you come to know about us?")
    # address = form
class CompanyData(models.Model):
    CHOICES = (
        ('w', 'Web Development' ),
        ('a', 'Coding' ),
        ('b', 'Analytics' ),
        ('c', 'Operations' ),
        ('d', 'Business Development' ),
        ('d', 'Design' ),
        ('e', 'Content Development' ),
        ('f', 'Product Development' ),
        ('g', 'Finance' ),
        ('h', 'Sales' ),
        ('i', 'Management Consulting' ),
        ('j', 'Others' ),
    )
    user = models.OneToOneField(CompanyProfile, on_delete=models.CASCADE, null=True)
    your_name = models.CharField(max_length=100, null=True)
    your_postion = models.CharField(max_length=100, null=True)
    name_of_founders = models.CharField(max_length=1000, null=True)
    description = models.CharField(max_length=1000, null=True)
    profiles_offered = MultiSelectField(max_length=1000, choices=CHOICES, null=True, editable=True)
    others = models.CharField(max_length=1000, null=True)
    number_of_vacancies = models.IntegerField(null=True)
    location = models.CharField(max_length=1000, null=True)
    stipend_offered = models.CharField(max_length=1000, null=True)
    work_profile_description = models.CharField(max_length=1000, null=True)
    other_incentive = models.CharField(max_length=1000, null=True)
    requirements = models.CharField(max_length=1000, null=True)
    reference = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.user.company_name
