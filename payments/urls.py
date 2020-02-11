from django.urls import path
from payments import views


app_name = "payments"

urlpatterns = [
    path('payfees/', views.payRegistrationFees, name="pay"),
    path('verify/', views.verifyPayment, name="verify")
]