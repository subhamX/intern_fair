from instamojo_wrapper import Instamojo
from accounts.models import StudentProfile
import pandas as pd
api = Instamojo(api_key="4a0095b9a6f22b83b9636b300d4295cd",
                auth_token="31c05e601dadb86742cf208c52d32dff")


response = api.payment_requests_list()
data = []
for payment_request in response['payment_requests']:
    if(payment_request['status']=="Completed"):
        id = payment_request['id']
        profiles = StudentProfile.objects.filter(order_id=id)
        if(profiles.count()):
            profile = profiles[0]
            if(not profile.reg_fees_paid):
                print(profile)
                data.append({
                    "name": profile.name,
                    "email": profile.email,
                })
            profile.reg_fees_paid = True
            profile.is_profile_complete = True
            profile.save()


pd.DataFrame(data).to_csv("success_but_changed_send_email.csv")