from instamojo_wrapper import Instamojo
from payments import cred as config

API_KEY = config.instamojo["api_key"]
AUTH_TOKEN = config.instamojo["auth_token"]

def payRegistration(payload):
    try:
        api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN)
        # api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')
        response = api.payment_request_create(
            amount='100',
            purpose='Intern Fair 2k20 IIT Ropar Student Registration',
            send_email=True,
            email=payload["email"],
            buyer_name= payload["name"],
            send_sms = True,
            phone= payload["phone_number"],
            redirect_url = payload["redirect_url"],
        )
        data = {
            "id": response['payment_request']['id'],
            "link": response['payment_request']['longurl'],
            "error":False
        }
        return data
    except Exception:
        return {"error": True}


def getPaymentLink(id):
    try:
        # api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')
        api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN)
        response = api.payment_request_status(id)
        if(response['payment_request']['status'] == "Completed"):
            status = True
        else:
            status= False
            
        data = {
            "status": status,
            "link": response['payment_request']['longurl'],
            "error": False
        }
        return data
    except Exception:
        return {"error": True}


'''

Function To Check The Payment Status.
PARAMS:
    Payment_ID
    Payment_Request_ID

'''
def getPaymentStatus(payment_id, payment_request_id):
    # api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/')
    api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN)
    response = api.payment_request_payment_status(payment_request_id, payment_id)
    if(response["success"]):
        if(response['payment_request']['payment']['status']=="Credit"):
            status= True
        else:
            status = False
        return status
    else:
        return False