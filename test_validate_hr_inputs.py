import pytest


@pytest.mark.parametrize("a", [
    {"patient_id": 1, "attending_email": 1},
    {"patient_id": 1, "attending_email": 1, "user_age": 1, "heart_rate": 1},
    {"patient_id": 1, "patient_id": 1},
    {"patient_id": 1},
])
def test_validate_hr_inputs(a):
    from validate_HR_inputs import validate_hr_inputs

    with pytest.raises(KeyError):
        validate_hr_inputs(a)
