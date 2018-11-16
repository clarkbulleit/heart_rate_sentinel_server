import pytest


@pytest.mark.parametrize("a,b,c,expected", [
    ([1, 2, 3, 4], 1, 1, 10/4),
    ([1, 1, 2], 1, 1, 4/3),
    ([1, 2], ["2018-11-15 17:28:01.657308", "2018-11-16 17:28:01.657308"], "2018-11-16 13:28:01.657308", 2)
])
def test_calc_avg_hr(a, b, c, expected):
    from calc_avg_hr import calc_avg_hr
    assert calc_avg_hr(a, b, c) == expected
