from operator import add, mul

import pytest

from fm2gp.matrix import Matrix
from fm2gp.power import power_semigroup


@pytest.mark.parametrize(
    'op,m,n,f',
    [
        (
            add,
            Matrix(1,1, [1]),
            3,
            Matrix(1,1, [3])
        ),
        (
            mul,
            Matrix(1,1, [2]),
            3,
            Matrix(1,1, [8])
        ),
        (
            mul,
            Matrix(2,2, [1,1,
                         1,0]),
            2,
            Matrix(2,2, [2,1,1,1])
        ),
    ]
)
def test_power_semigroup(op, m, n, f):
    assert n > 0
    r = power_semigroup(m, n, op)

    assert r == f
