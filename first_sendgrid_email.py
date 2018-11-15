# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *


def send_email(patient_id, timestamp):
    sg = sendgrid.SendGridAPIClient(apikey='SG.lpj1iTqMRtmDXd5GCxoiHQ.'
                                           'rXDJvAce_fNivEwZMKC53uIE9Quq-ocTHAX9wgUAwzg')
    from_email = Email("clark.bulleit@duke.edu")
    to_email = Email("clarkbulleit@gmail.com")
    subject = "Patient {} is tachycardic".format(patient_id)
    content = Content("text/plain", "Patient is tachycardic at {}".format(timestamp))
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
