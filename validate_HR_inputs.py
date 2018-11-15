
def validate_hr_inputs(r):
    hr_keys = [
        "patient_id",
        "heart_rate",
    ]

    for key in hr_keys:
        if key not in r.keys() or len(r.keys()) != 2:
            raise KeyError
