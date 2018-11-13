from pymodm import connect
connect("mongodb://<dbuser>:<dbpassword>@ds037778.mlab.com:37778/patients_cb329")

class patient(MongoModel):
    email = fields.EmailField(primary_key=True)
    first_name = fields.CharField()
    last_name = fields.CharField()
    password = fields.CharField()


