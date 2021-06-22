from twilio.rest import Client 
import os

account_sid = os.environ("account_sid")
auth_token = os.environ("auth_token")
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Hello! This is my first trial for twilio API",
                    from_='+15053374593',
                    to='+999999999999'
                )

print(message.sid)

