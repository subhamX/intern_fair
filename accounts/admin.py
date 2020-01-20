from django.contrib import admin
from accounts import models
# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.CompanyProfile)
admin.site.register(models.StudentProfile)