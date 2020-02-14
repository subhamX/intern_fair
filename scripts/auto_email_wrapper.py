from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64
from apiclient import errors

BASE_DIR = os.getcwd()

SCOPES = ['https://mail.google.com/',
          'https://www.googleapis.com/auth/gmail.compose',
          'https://www.googleapis.com/auth/gmail.modify',
          'https://www.googleapis.com/auth/gmail.send']


def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                .execute())
        print('Message Id:' + message['id'])
        print(message)
        return True
    except errors.HttpError as error:
        print('An error occurred:' + str(error))
        return False

def sendEmail(to, subject, message_text, sender='ecell@iitrpr.ac.in'):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(os.path.join(BASE_DIR,
                'credentials.json'), SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    temp = create_message(sender, to, subject, message_text)
    return send_message(service,'me', temp)

name = "Subham"
message = 'Dear ' + name + '\n\nYour profile status has been changed to complete. But do ensure that you have uploaded a CV. You can now go to portal and apply in companies.\n\nRegards\nTechnical Team, Ecell'
sendEmail("idevsubham@gmail.com", "Intern Fair: Profile Status Updated", message)


# send_message(service,'me',k)
# sendEmail("idevsubham@gmail.com", "Reminder: Few Hours Left| Intern Fair, Ecell", message)

