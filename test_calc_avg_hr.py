import pytest


@pytest.mark.parametrize("a, expected", [
    ([1, 2, 3, 4], 10/4),
    ([1, 1, 2], 4/3),
])
def test_calc_avg_hr(a, expected):
    from calc_avg_hr import calc_avg_hr
    assert calc_avg_hr(a) == expected
