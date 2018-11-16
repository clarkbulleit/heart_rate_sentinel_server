
def validate_post_inputs(r, route):
    if route == 1:
        patient_keys = [
            "patient_id",
            "attending_email",
            "user_age"
            ]
    elif route == 2:
        patient_keys = [
            "patient_id",
            "heart_rate",
            ]

    for key in patient_keys:
        if key not in r.keys() or len(r.keys()) != len(patient_keys):
            raise KeyError
