from patients import Patient


def validate_get_request(patient_id):
    try:
        int(patient_id)
    except ValueError:
        return 0

    try:
        p = Patient.objects.raw({"_id": int(patient_id)}).first()
    except Patient.DoesNotExist:
        return 1

    hr = p.heart_rate
    if not hr:
        return 2
    else:
        return hr
