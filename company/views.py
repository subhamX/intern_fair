from django.shortcuts import render, reverse
from company import forms
from django.http import HttpResponseRedirect
from company import models
from accounts import models as accountModels
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required



def guidelines(request):
    return render(request, 'company/guidelines.html')

    
def profile(request):
    # Checking If the User is already Logged In
    if(not request.user.is_authenticated):
        return HttpResponseRedirect(reverse("home"))
    else:
        profile = accountModels.Profile.objects.filter(user=request.user)
        if(profile[0].is_student):
            return HttpResponseRedirect(reverse("home"))

    message = ''
    success_msg = ''    
    if( request.method == 'POST'):
        form = forms.CompanyDataForm(request.POST)
        if( form.is_valid() ):
            instance = form.save(commit=False)
            instance.user = models.CompanyProfile.objects.get(user=request.user)
            instance.save()
            return HttpResponseRedirect(reverse("company:profile"))
    else:
        formData = models.CompanyData.objects.filter(user=models.CompanyProfile.objects.get(user=request.user))
        if(formData.count()):
            # Display Data
            data = formData.values()[0]
            form = forms.CompanyDataForm(data=data)
            context = {
                "form": form
            }
            return render(request, 'company/display_profile.html', context)
        else:
            form = forms.CompanyDataForm()
                
    context = {
        'form': form,
        'error_msg': message,
        'success_msg': success_msg,
    }
    return render(request, 'company/profile.html', context)