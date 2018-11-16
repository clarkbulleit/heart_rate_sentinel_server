import pytest
from validate_GET_request import validate_get_request


@pytest.mark.parametrize("a,expected", [
    ('a', 0),
    (7, 1),
    (5, 2)
])
def test_validate_get_request(a, expected):

    assert validate_get_request(a) == expected
