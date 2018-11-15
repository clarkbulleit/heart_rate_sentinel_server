import pytest


@pytest.mark.parametrize("a, b, expected", [
    (160, 12, True),

])
def test_is_tachycardic(a, b, expected):
    from is_tachycardic import is_tachycardic

    assert is_tachycardic(a, b) == expected
