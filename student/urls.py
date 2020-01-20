from django.contrib import admin
from django.urls import path
from accounts import views

app_name = 'student'

urlpatterns = [
    path('', views.companySignUpView, name='home'),
    # path('login/', views.loginView, name='signin'),
    # path('logout/', views.logoutView, name='logout'),
]
