from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    # if True then the user is student
    is_student = models.BooleanField(default=True) 


class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.IntegerField()
    website_link = models.URLField()

class StudentProfile(models.Model):
    name = models.CharField(max_length=100)
    entry_number=models.CharField(max_length=200)
    email = models.EmailField()
    contact_number = models.IntegerField()
    college_year=models.IntegerField()