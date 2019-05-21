from operator import add, mul

import pytest

from fm2gp.power import power_accumulate
from fm2gp.power import power_semigroup
from fm2gp.power import half


@pytest.mark.parametrize(
    "x,n,e",
    [
        (3, 0, 0),
        (5.0, 1, 5.0),
        (9, 4, 36),
    ]
)
def test_power_accumulate_add(x, n, e):
    r = 0
    r = power_accumulate(r, x, n, add)
    assert r == e
    assert type(x) == type(r)


def test_half():
    assert half(3) == 1
    assert half(8) == 4


@pytest.mark.parametrize(
    "x,n,e",
    [
        (3, 7, 21),
        (5.0, 1, 5.0),
        (9, 4, 36),
    ]
)
def test_power_add(x, n, e):
    r = power_semigroup(x, n, add)
    assert r == e
    assert type(x) == type(r)
