
class PatientKeyError(Exception):
    def __init__(self, message):
        self.message = message


def validate_inputs(r):
    patient_keys = [
        "patient_id", "attending_email", "user_age"
    ]
    for key in patient_keys:
        if key not in r.keys():
            raise PatientKeyError("Key '{0}' not present in request".format(key))
