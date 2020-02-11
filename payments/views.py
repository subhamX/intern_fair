from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from payments import gateway
from accounts import models
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url = "/accounts/signin/")
def verifyPayment(request):
    payment_id = request.GET.get("payment_id")
    payment_request_id = request.GET.get("payment_request_id")
    # Checking The Status Of Payment
    status = gateway.getPaymentStatus(payment_id, payment_request_id)
    if(status):
        # If Status is True
        instance = models.StudentProfile.objects.filter(order_id=payment_request_id, user=request.user)
        if(instance.count()):
            profile = instance[0]
            profile.reg_fees_paid = True
            profile.save()
            return HttpResponseRedirect(reverse("student:profile"))
        else:
        # If Status is False, Redirecting To Error Page
            return render(request, "error.html")
    else:
        # Invalid params
        return render(request, "error.html")



@login_required(login_url = "/accounts/signin/")
def payRegistrationFees(request):
    queryset = models.StudentProfile.objects.filter(user = request.user)
    if(queryset.count()):
        # Student Registration
        instance = queryset[0]
        # Student Has Paid The Fees
        if(instance.reg_fees_paid):
            return reverse("student:profile")
        if(instance.order_id):
            res = gateway.getPaymentLink(instance.order_id)
            if(res["error"]):
                return render(request, "error.html")

            if(res["status"]):
                # Changing The Paid Status To True 
                instance.reg_fees_paid = True
                instance.save()
                return HttpResponseRedirect(reverse("student:profile"))
            else:
                # Redirecting To Payment Gateway
                url = res["link"]
                return redirect(url)

        redirect_url = request.build_absolute_uri('/payments/verify/')
        payload = {
            "name": instance.name,
            "email": instance.email,
            "phone_number": instance.contact_number,
            "redirect_url": redirect_url
        }
        res = gateway.payRegistration(payload)
        id = res["id"]
        instance.order_id = id
        instance.save()
        url = res["link"]
        return redirect(url)
    else:
        return render(request, "error.html")

