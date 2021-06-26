import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("khushi.sharma.2201@gmail.com")
to_email = To("khushi.sharma.2201@gmail.com")
subject = "First trial of Sendgrid"
content = Content("text/plain", "First mail of sendgrid! ")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
