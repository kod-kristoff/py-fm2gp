from operator import add, mul

import pytest

from fm2gp.power import power_accumulate


@pytest.mark.parametrize(
    "x,n,e",
    [
        (3, 0, 0),
        (5.0, 1, 5.0),
        (9, 4, 36),
    ]
)
def test_power_add(x, n, e):
    r = 0
    r = power_accumulate(r, x, n, add)
    assert r == e
    assert type(x) == type(r)
