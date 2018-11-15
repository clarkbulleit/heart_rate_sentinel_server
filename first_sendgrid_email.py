# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey='SG.lpj1iTqMRtmDXd5GCxoiHQ.'
                                       'rXDJvAce_fNivEwZMKC53uIE9Quq-ocTHAX9wgUAwzg')
from_email = Email("clarkbulleit@gmail.com")
to_email = Email("clark.bulleit@duke.edu")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
