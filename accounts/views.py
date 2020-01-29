from django.shortcuts import render, reverse
from accounts import forms
from django.http import HttpResponseRedirect
from accounts import models
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required



def checkAndRedirect(user):
    profileInstance = models.Profile.objects.get(user=user)
    if( profileInstance.is_student == True):
        return HttpResponseRedirect(reverse('student:home'))
    else:
        return HttpResponseRedirect(reverse('company:home'))



def loginView(request):
    # Checking If the User is already Logged In
    message = ''
    if( request.user.is_authenticated ):
        return checkAndRedirect(request.user)
    if( request.method == 'POST'):
        form = forms.LoginForm(request.POST)
        if( form.is_valid() ):
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if( user ):
                login(request, user)
                return checkAndRedirect(request.user)
            else:
                message = 'Invalid Username Or Password'
                
    context = {
        'form': forms.LoginForm(),
        'error_msg': message,
    }
    return render(request, 'accounts/signin.html', context)



def companySignUpView(request):
    if( request.user.is_authenticated ):
        return HttpResponseRedirect(reverse('home'))
    error_msg = ""
    if( request.method == 'POST'):
        form = forms.CompanySignUpForm(request.POST)
        if( form.is_valid() ):
            print(form.cleaned_data['email'])
            instance = form.save(commit=False)
            # Only after instance is saved We can access id
            instance.save()

            
            old_user = User.objects.filter(username=form.cleaned_data['email'])
            if(old_user):
                error_msg = "User with specified Email Id Already Exists"
            else:
                user = User(username=form.cleaned_data['email'])
                user.set_password(form.cleaned_data['password'])
                user.save()
                # Creating Profile Instance for the new user as student
                profileInstance = models.Profile(is_student=False)
                profileInstance.user = user
                profileInstance.save()
                user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
                if( user ):
                    login(request, user)
                    message = "You are successfully registered"
                    return HttpResponseRedirect(reverse('company:profile'))

    else:
        form = forms.CompanySignUpForm()
    return render(request, 'accounts/company/signup.html', {"form": form, "error_msg": error_msg}) 

def studentSignUpView(request):
    if( request.user.is_authenticated ):
        return HttpResponseRedirect(reverse('home'))
    error_msg = ""
    if( request.method == 'POST'):
        form = forms.StudentSignUpForm(request.POST)
        if( form.is_valid() ):
            print(form.cleaned_data['email'])
            instance = form.save(commit=False)
            # Only after instance is saved We can access id
            instance.save()


            old_user = User.objects.filter(username=form.cleaned_data['email'])
            if(old_user):
                error_msg = "User with specified Email Id Already Exists"
            else:
                user = User(username=form.cleaned_data['email'])
                user.set_password(form.cleaned_data['password'])
                user.save()
                # Creating Profile Instance for the new user as student
                profileInstance = models.Profile(is_student=True)
                profileInstance.user = user
                profileInstance.save()
                user = authenticate(request, username=form.cleaned_data['email'], password=form.cleaned_data['password'])
                if( user ):
                    login(request, user)
                    message = "You are successfully registered"
                    return HttpResponseRedirect(reverse('student:profile'))
    else:
        form = forms.StudentSignUpForm()
    return render(request, 'accounts/student/signup.html', {"form": form, "error_msg": error_msg}) 



@login_required(login_url='/accounts/login/')
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
