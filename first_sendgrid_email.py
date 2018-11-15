# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
from sendgrid.helpers.mail import *


def send_email(patient_id, timestamp):
    sg = sendgrid.SendGridAPIClient(apikey='Sendgrid_API_Key')
    from_email = Email("clark.bulleit@duke.edu")
    to_email = Email("clarkbulleit@gmail.com")
    subject = "Patient {} is tachycardic".format(patient_id)
    content = Content("text/plain", "Patient is tachycardic at {}"
                      .format(timestamp))
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
