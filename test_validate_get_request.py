import pytest
from validate_GET_request import validate_get_request


@pytest.mark.parametrize("a,expected", [
    ('a', 0),
    (10000, 1),
    (5, 2),
    (1, 3),
    (2, 3),
])
def test_validate_get_request(a, expected):

    assert validate_get_request(a) == expected
