from django.db import models
from django.contrib.auth.models import User




class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)
    website_link = models.URLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class StudentProfile(models.Model):
    CHOICES = (
        (1, '1st Year'),
        (2, '2nd Year'),
        (3, '3rd Year'),
        (4, '4th Year'),
    )
    name = models.CharField(max_length=100)
    entry_number=models.CharField(max_length=200)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)
    college_year=models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)



# Create your models here.
class Profile(models.Model):
    # if True then the user is student
    is_student = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # company_profile = models.OneToOneField(CompanyProfile, on_delete=models.CASCADE, null=True)
    # student_profile = models.OneToOneField(StudentProfile, on_delete=models.CASCADE, null=True)
