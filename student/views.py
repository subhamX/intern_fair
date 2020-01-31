from django.shortcuts import render, reverse
from company import forms
from django.http import HttpResponseRedirect
from company import models
from accounts import models as accountModels
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def guidelines(request):
    return render(request, 'student/guidelines.html')


def profile(request):
    # Checking If the User is already Logged In
    if(not request.user.is_authenticated):
        return HttpResponseRedirect(reverse("home"))
    else:
        profile = accountModels.Profile.objects.filter(user=request.user)
        if(profile[0].is_student):
            message = ''
            context = {
                'message': message
            }
            return render(request, 'message.html', context)
    
    
    # success_msg = ''    
    # mark_flag = False
    # if( request.method == 'POST'):
    #     form = forms.CompanyDataForm(request.POST)
    #     if( form.is_valid() ):
    #         print(form)
    #         formData = models.CompanyData.objects.filter(uid=request.user)
    #         if(formData.count()):
    #             formData[0].address = form.cleaned_data.get('address')
    #             formData[0].your_name = form.cleaned_data.get('your_name')
    #             formData[0].your_postion = form.cleaned_data.get('your_postion')
    #             formData[0].description = form.cleaned_data.get('description')
    #             formData[0].profiles_offered = form.cleaned_data.get('profiles_offered')
    #             formData[0].others = form.cleaned_data.get('others')
    #             formData[0].save()
    #             mark_flag = True
    #             success_msg = "Form Saved Successfully"

    #         else:
    #             instance = form.save(commit=False)
    #             instance.uid = request.user
    #             instance.save()
    #             mark_flag = True
    #             success_msg = "Form Saved Successfully"
    # else:
    #     formData = models.CompanyData.objects.filter(uid=request.user)
    #     if(formData.count()):
    #         print(formData[0])
    #         address = formData[0].address
    #         your_name = formData[0].your_name
    #         your_postion = formData[0].your_postion
    #         description = formData[0].description
    #         profiles_offered = formData[0].profiles_offered
    #         others = formData[0].others
    #         contact_number = formData[0].contact_number
    #         mark_flag = True
    #         form = forms.CompanyDataForm(data={'address': address, 'your_name': your_name, 'your_postion': your_postion, 'description': description, 'profiles_offered':profiles_offered, others:others, 'contact_number': contact_number })
    #     else:
    #         form = forms.CompanyDataForm()
                
    # context = {
    #     'form': form,
    #     'error_msg': message,
    #     'success_msg': success_msg,
    #     'mark_flag': mark_flag
    # }
    # return render(request, 'company/profile.html', context)