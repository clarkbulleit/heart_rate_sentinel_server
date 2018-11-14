import pytest


@pytest.mark.parametrize("a", [
    {"patient_id": 1, "attending_email": 1},
    {"_id": 1, "attending_email": 1, "user_age": 1},
    {"patient_id": 1, "attending_email": 1, "user_age": 1, "ad": 1},
])


def test_validate_inputs(a):
    from validate_inputs import validate_inputs

    with pytest.raises(KeyError):
        validate_inputs(a)



