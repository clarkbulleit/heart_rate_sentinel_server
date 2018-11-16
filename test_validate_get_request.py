import pytest
from validate_GET_request import validate_get_request
from patients import Patient
from pymodm import connect


@pytest.mark.parametrize("a,expected", [
    (50, 3),
    (51, 2),
    (52, 1),
    ('a', 0),
    (' ', 0),
    (1.75, 0)
])
def test_validate_get_request(a, expected):
    connect("mongodb://clarkbulleit:goduke112@ds037778.mlab.com:"
            "37778/patients_cb329")

    if a == 50:
        p = Patient(a, attending_email='clark@gmail.com',
                    user_age=50, heart_rate=[1])
        p.save()
    elif a == 51:
        p = Patient(a, attending_email='clark@gmail.com',
                    user_age=50)
        p.save()

    assert validate_get_request(a) == expected

    if a == 50 or a == 51:
        p1 = Patient.objects.raw({"_id": a}).first()
        p1.delete()
