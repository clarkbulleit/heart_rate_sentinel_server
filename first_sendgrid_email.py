# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
from sendgrid.helpers.mail import *


def send_email(attending_email, patient_id, timestamp):
    """ Sends email to attending_email if patient is tachycardic

    Args:
        attending_email (str): email of attending doctor
        patient_id (int): patient id number
        timestamp (str): Time the data is input into function

    Returns:
        Email to attending doctor from clark.bulleit@duke.edu
    """
    sg = sendgrid.SendGridAPIClient(apikey='SG.lpj1iTqMRtmDXd5GC'
                                           'xoiHQ.rXDJvAce_fNivEw'
                                           'ZMKC53uIE9Quq-ocTHAX9w'
                                           'gUAwzg')
    from_email = Email("clark.bulleit@duke.edu")
    to_email = Email(attending_email)
    subject = "Patient {} is tachycardic".format(patient_id)
    content = Content("text/plain", "Patient is tachycardic at {}"
                      .format(timestamp))
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
