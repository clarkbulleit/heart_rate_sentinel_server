
def validate_inputs(r):
    patient_keys = [
        "patient_id", "attending_email", "user_age"
    ]
    for key in patient_keys:
        if key not in r.keys() or len(r.keys()) != 3:
            raise KeyError
