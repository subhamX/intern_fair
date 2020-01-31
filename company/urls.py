from django.contrib import admin
from django.urls import path
from company import views

app_name = 'company'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('guidelines/', views.guidelines, name='guidelines'),
]
