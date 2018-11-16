import pytest


@pytest.mark.parametrize("a,b,c,expected", [
    ([1, 2, 3, 4], 1, 1, 10/4),
    ([1, 1, 2], 1, 1, 4/3),
])
def test_calc_avg_hr(a, b, c, expected):
    from calc_avg_hr import calc_avg_hr
    assert calc_avg_hr(a, b, c) == expected
