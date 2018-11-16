import pytest
from validate_GET_request import validate_get_request


def test_validate_get_request():
    patient_id = 1

    assert validate_get_request(patient_id) == ([140], 1)
