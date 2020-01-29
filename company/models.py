from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
# Create your models here.

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
    )
    address = models.CharField(max_length=1000, null=True)
    your_name = models.CharField(max_length=100, null=True)
    your_postion = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=1000, null=True)
    profiles_offered = MultiSelectField(max_length=1000, choices=CHOICES, null=True, editable=True)
    others = models.CharField(max_length=1000, null=True)
    contact_number = models.IntegerField()
    uid = models.OneToOneField(User, on_delete=models.CASCADE)