from django.contrib import admin
from django.urls import path
from student import views

app_name = 'student'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    # path('login/', views.loginView, name='signin'),
    # path('logout/', views.logoutView, name='logout'),
]
