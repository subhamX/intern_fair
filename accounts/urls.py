from django.contrib import admin
from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('c/signup/', views.companySignUpView, name='company_signup'),
    path('s/signup/', views.studentSignUpView, name='student_signup'),
    path('logout/', views.logoutView, name='logout'),
]
