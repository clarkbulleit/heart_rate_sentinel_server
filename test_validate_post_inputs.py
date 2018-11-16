import pytest


@pytest.mark.parametrize("a, route", [
    ({"patient_id": 1, "attending_email": 1}, 1),
    ({"_id": 1, "attending_email": 1, "user_age": 1}, 1),
    ({" patient_id": 1, "attending_email": 1, "user_age": 1}, 1),
    ({" patient_id": 1, "attending_email": 1, "user_age": 1, "ds": 1}, 1),
    ({" patient_id": 1, "attending_email": 1, "user_age": 1,
      "patient_id": 1}, 1),
    ({" patient_id": 1, "attending_email": 1, "patient_id": 1}, 1),
    ({"patient_id": 1, "attending_email": 1}, 2),
    ({"patient_id": 1, "attending_email": 1, "user_age": 1,
      "heart_rate": 1}, 2),
    ({"patient_id": 1, "patient_id": 1}, 2),
    ({"patient_id": 1}, 2),
])
def test_validate_post_inputs(a, route):
    from validate_post_inputs import validate_post_inputs

    with pytest.raises(KeyError):
        validate_post_inputs(a, route)
