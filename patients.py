from pymodm import connect
from pymodm import MongoModel, fields

connect("mongodb://clarkbulleit:goduke112@ds037778."
        "mlab.com:37778/patients_cb329")


class Patient(MongoModel):
    patient_id = fields.IntegerField(primary_key=True)
    attending_email = fields.EmailField()
    user_age = fields.IntegerField()
    heart_rate = fields.ListField()
    time = fields.ListField()
    is_tachycardic = fields.BooleanField()
