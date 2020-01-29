from django.shortcuts import render, reverse
from accounts import forms
from django.http import HttpResponseRedirect
from accounts import models
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def home(request):
    message = ""
    return render(request, 'base/index.html', {"message": message}) 


def profile(request):
    if(request.user.is_authenticated):
        profile = models.Profile.objects.get(user=request.user)
        if(profile.is_student):
            return HttpResponseRedirect(reverse('student:profile'))
        else:
            return HttpResponseRedirect(reverse('company:profile'))
    else:
        return HttpResponseRedirect(reverse('home'))

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
                    return HttpResponseRedirect(reverse('student:home'))
    else:
        form = forms.StudentSignUpForm()
    return render(request, 'accounts/student/signup.html', {"form": form, "error_msg": error_msg}) 


