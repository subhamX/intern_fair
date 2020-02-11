from instamojo_wrapper import Instamojo
import cred as config

API_KEY = config.instamojo["api_key"]
AUTH_TOKEN = config.instamojo["auth_token"]


def payRegistration(payload):
    api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN)
    response = api.payment_request_create(
        amount='100',
        purpose='Intern Fair 2k20 IIT Ropar Student Registration',
        send_email=True,
        email=payload["email"],
        buyer_name= payload["name"],
        send_sms = True,
        phone= payload["phone_number"],
        webhook = "https://internfair.ecelliitrpr.com/payments/verify/",
        redirect_url = "https://internfair.ecelliitrpr.com/profile/",
    )
    print (response['payment_request']['id'])
    print (response['payment_request']['longurl'])
    data = {
        "id": response['payment_request']['id'],
        "link": response['payment_request']['longurl']
    }
    return data


def getPaymentStatus(id):
    api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN)
    response = api.payment_request_status(id)
    print(response['payment_request']['shorturl'])


getPaymentStatus('54ed40171a664f2090ffbc1f8e41936e')