from django.contrib import admin
from company import models
# Register your models here.

admin.site.register(models.CompanyData)
admin.site.register(models.ApplyProfile)
admin.site.register(models.RegCompany)