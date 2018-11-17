
def validate_post_inputs(r, route):
    """ Validates input keys for 3 POST routes

    This function works for all 3 POST routes
    and  works based on the route number
    1: add_patient POST route
    2: heart_rate POST route
    3: heart_rate/interval_average POST route

    Args:
        r (dict): dictionary parsed from POST input
        route (int): Route number key

    Returns:
        Error: KeyError if keys are not valid for the corresponding route
    """
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
    elif route == 3:
        patient_keys = [
            "patient_id",
            "heart_rate_average_since",
        ]

    for key in patient_keys:
        if key not in r.keys() or len(r.keys()) != len(patient_keys):
            raise KeyError
