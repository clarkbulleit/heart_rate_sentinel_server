import pytest


@pytest.mark.parametrize("a, b, expected", [
    (160, 12, True),
    (138, 4, True),
    (135, 5, True),
    (129, 5, False),
    (70, 40, False)
])
def test_is_tachycardic(a, b, expected):
    from is_tachycardic import is_tachycardic

    assert is_tachycardic(a, b) == expected
