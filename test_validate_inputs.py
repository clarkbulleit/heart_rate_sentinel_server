
def test_validate_inputs():
    import pytest
    from validate_inputs import validate_inputs

    bad_input1 = {"patient_id": 1, "attending_email": 1}

    with pytest.raises(KeyError):
        validate_inputs(bad_input1)


