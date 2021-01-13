from twilio.rest import Client 
import os

account_sid = 'ACcd5a9adfec7841de4b4ba576987852d6'
auth_token = '2ddddc74a05ba543d5d47288d6a05490'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Hello! This is my first trial for twilio API",
                    from_='+15053374593',
                    to='+91 97114 85949'
                )

print(message.sid)

