from django.contrib import admin
from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('c/signup/', views.companySignUpView, name='company_signup'),
    path('s/signup/', views.studentSignUpView, name='student_signup'),
    # path('login/', views.loginView, name='signin'),
    # path('logout/', views.logoutView, name='logout'),
]
