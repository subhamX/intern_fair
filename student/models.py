from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
# Create your models here.

class StudentData(models.Model):
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
    
    # name = models.CharField(max_length=100)
    # entry_number=models.CharField(max_length=200)
    # email = models.EmailField()
    # contact_number = models.IntegerField()
    # college_year=models.IntegerField()