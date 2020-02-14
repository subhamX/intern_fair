from django.db import models
from multiselectfield import MultiSelectField
from accounts.models import CompanyProfile, StudentProfile

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

class ApplyProfile(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    applied_roles = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.student.name


class RegCompany(models.Model):
    id = models.IntegerField(primary_key=True, default=100)
    name = models.CharField(max_length=1000)
    apply_profile = models.ManyToManyField(ApplyProfile, blank=True)
    def __str__(self):
        return self.name