from patients import Patient


def validate_get_request(patient_id):
    """ Validates inputs for all get requests in route

    Function will return code that corresponds to an error
    message.
    0: Integer not entered
    1: Patient doesnt exist
    2: Heart rate list is empty
    3: Request is valid

    :param patient_id: Integer
    :return: Code 0-3
    """

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
        return 3
