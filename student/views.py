from django.shortcuts import render, reverse
from company import forms
from django.http import HttpResponseRedirect, JsonResponse
from company import models
from accounts import models as accountModels
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from accounts import forms as accountForms
# Create your views here.

profiles_offered_by_company = [
    {
        'label': "1_option",
        'options': ['Content Development', 'Design', 'Business Development', 'Product Development']
    },
    {
        'label': "2_option",
        'options': ['Web Development', 'Coding', 'Analytics', 'Product Development']
    },
    {
        'label': "3_option",
        'options': ['Web Development', 'Coding', 'Business Development', 'Product Development', 'Design', 'Content Development', 'Others (Drones,Robotics, ROS, Ai/Data Science)']
    },
    {
        'label': "4_option",
        'options': ['Web Development', 'Analytics', 'Product Development', 'Business development', 'Design', 'Finance', 'Sales', 'Management Consulting']
    },
    {
        'label': "5_option",
        'options': ['Business development', 'Design', 'Others (Electronics, Material Science, Mechanical)']
    },
    # {'3_options': ['Content Development', 'Design', 'Business Development', 'Product Development']},
        # ['Content1 Development', 'Design', 'Business Development', 'Product Development'],
]

def getProfilesOffered(request):
    # serialized = serializers.serialize('json', profiles_offered_by_company)
    return JsonResponse(profiles_offered_by_company, safe=False)

def catalog(request):
    flag= False
    context = {}
    if(request.user.is_authenticated):
        queryset = accountModels.StudentProfile.objects.filter(user=request.user)
        message = ""
        if(queryset.count()):
            if(not queryset[0].is_profile_complete):
                message="Please complete your profile and pay your registration fees to apply!"
                flag=False
            else:
                flag=True
        url = request.build_absolute_uri('/s/profilesoffered/')
        posturl = request.build_absolute_uri('/s/register/')
        context = {
            "show_apply" : flag,
            "complete_profile_message": message,
            "fetch_endpoint": url,
            "post_endpoint": posturl,
        }
    
    return render(request, "startup/catalog.html", context)

# http://localhost:8000/s/register/1/?options=2_3
@login_required(login_url="/accounts/signin/")
def register_for_company(request, id):
    queryset = accountModels.StudentProfile.objects.filter(user=request.user)
    if(queryset.count()):
        if(not queryset[0].is_profile_complete):
            return HttpResponseRedirect(reverse("student:profile"))

        try:
            instance = models.RegCompany.objects.get(id=id)
            a = request.GET.get("options")
            if(not a):
                return render(request, "error.html")
            options_index = a.split("_")
            applied_profiles = ""
            for label, option in enumerate(options_index):
                applied_profiles += str(label) + "-" + profiles_offered_by_company[id-1]["options"][int(option)] + "\n"
            student_set = instance.apply_profile.filter(student=queryset[0])
        except Exception:
            return render(request, "error.html")
        if(student_set.count()):
            flag=True
        else:     
            applyProfileInstance = models.ApplyProfile(applied_roles=applied_profiles, student= queryset[0])
            applyProfileInstance.save()
            instance.apply_profile.add(applyProfileInstance)
            instance.save()
            flag=False
        context = {
            'name': queryset[0].name,
            'company_name': instance.name,
            'already_applied': flag
        }
        return render(request, "startup/success.html", context)
    else:
        return render(request, "error.html")


def guidelines(request):
    return render(request, 'student/guidelines.html')

@login_required(login_url="/accounts/signin/")
def profile(request):
    # Checking If the User is already Logged In

    if(request.method=="POST"):
        form = accountForms.UploadCVForm(request.POST, request.FILES)
        if form.is_valid():
            instance = accountModels.StudentProfile.objects.get(user=request.user)
            instance.cv = request.FILES['cv']
            if(instance.reg_fees_paid==True):
                instance.is_profile_complete = True
            instance.save()
            return HttpResponseRedirect(reverse("student:profile"))
    else:
        form = accountForms.UploadCVForm()

        profile = accountModels.Profile.objects.filter(user=request.user)
        if(profile[0].is_student):
            pro = accountModels.StudentProfile.objects.get(user=request.user)
            if(pro.cv):
                uploadedFlag = True
            else:
                uploadedFlag = False
            
            if(pro.is_profile_complete):
                pro_complete = True
            else:
                pro_complete = False
            print(pro_complete)
            data = [
                {"label": "Name", "value": pro.name},
                {"label": "Email", "value": pro.email},
                {"label": "Contact Number", "value": pro.contact_number},
                {"label": "College Year", "value": pro.college_year},
            ]
            context = {
                "data": data,
                "order_status": pro.reg_fees_paid,
                "form": form,
                "uploadedFlag": uploadedFlag,
                "pro_complete": pro_complete
            }
            # print(type(profile[0]))
            # print(dir(profile[0]))
            # for entry in profile[0]:
            #     print(entry)
            return render(request, 'student/display_profile.html', context)
    
    
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