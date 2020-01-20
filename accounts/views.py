from django.shortcuts import render, reverse
from accounts import forms
from django.http import HttpResponseRedirect
from accounts import models
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# def loginView(request):
#     # Checking If the User is already Logged In
#     message = ''
#     if( request.method == 'POST'):
#         form = forms.LoginForm(request.POST)
#         if( form.is_valid() ):
#             user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#             if( user ):
#                 login(request, user)
#                 return checkAndRedirect(request.user)
#             else:
#                 message = 'Invalid Username Or Password'
                
#     return render(request, 'accounts/signin.html', context)



@login_required(login_url='/accounts/login/')
def logoutView(request):
    logout(request)
    return render(request, 'accounts/logout.html')


def companySignUpView(request):
    error_msg = ""
    if( request.method == 'POST'):
        form = forms.CompanySignUpForm(request.POST)
        if( form.is_valid() ):
            print(form.cleaned_data['email'])
            instance = form.save(commit=False)
            # Only after instance is saved We can access id
            instance.save()

            # Creating Profile Instance for the new user as student
            profileInstance = models.Profile(is_student=False)
            profileInstance.save()
            old_user = User.objects.filter(username=form.cleaned_data['email'])
            if(old_user):
                error_msg = "User with specified Email Id Already Exists"
            else:
                user = User(username=form.cleaned_data['email'])
                user.set_password(form.cleaned_data['password'])
                user.save()
                user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
                if( user ):
                    login(request, user)
                    message = "You are successfully registered"
                    return HttpResponseRedirect(reverse('main:home', args=(message,)))
    else:
        form = forms.CompanySignUpForm()
    return render(request, 'accounts/company/signup.html', {"form": form, "error_msg": error_msg}) 

def studentSignUpView(request):
    error_msg = ""
    if( request.method == 'POST'):
        form = forms.StudentSignUpForm(request.POST)
        if( form.is_valid() ):
            print(form.cleaned_data['email'])
            instance = form.save(commit=False)
            # Only after instance is saved We can access id
            instance.save()

            # Creating Profile Instance for the new user as student
            profileInstance = models.Profile(is_student=True)
            profileInstance.save()
            old_user = User.objects.filter(username=form.cleaned_data['email'])
            if(old_user):
                error_msg = "User with specified Email Id Already Exists"
            else:
                user = User(username=form.cleaned_data['email'])
                user.set_password(form.cleaned_data['password'])
                user.save()
                user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
                if( user ):
                    login(request, user)
                    message = "You are successfully registered"
                    return HttpResponseRedirect(reverse('home', args=(message,)))
    else:
        form = forms.StudentSignUpForm()
    return render(request, 'accounts/student/signup.html', {"form": form, "error_msg": error_msg}) 