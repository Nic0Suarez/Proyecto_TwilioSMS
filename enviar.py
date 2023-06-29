
import os
from twilio.rest import Client
from twilio_config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, PHONE_NUMBER
from config_sms import dataFrame_msj , dataFrame

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body=dataFrame_msj.all,
         from_=PHONE_NUMBER,
         to='+543764151300'
     )

print(message.sid)
print('Mensaje Enviado Exitosamente')