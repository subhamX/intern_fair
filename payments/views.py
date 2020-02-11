from django.shortcuts import render, redirect
from payment import gateway
from accounts import models
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url = "/accounts/signin/")
def payRegistrationFees(request):
    user = request.user
    profileInstance = models.Profile.objects.get(user=user)
    if(profileInstance.is_student):
        # Student Registration
        instance = models.StudentProfile.objects.get(user = request.user)
        payload = {
            "name": instance.name,
            "email": instance.email,
            "phone_number": instance.contact_number,
            "desc": ""
        }
        res = gateway.payRegistration(payload)
        id = res["id"]
        instance.order_id = id
        instance.save()
        url = res["link"]
        return redirect(url)
    else:
        return render(request, "error.html")

