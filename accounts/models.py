from django.db import models
from django.contrib.auth.models import User




class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.CharField(max_length=10)
    website_link = models.URLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.company_name

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
    reg_fees_paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=1000, null=True)
    
    def __str__(self):
        return self.name


# Create your models here.
class Profile(models.Model):
    # if True then the user is student
    is_student = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
