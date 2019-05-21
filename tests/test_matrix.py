import pytest

from fm2gp.matrix import Matrix


def test_index():
    m = Matrix(2, 3)

    for c in range(3):
        for r in range(2):
            assert m[r, c] == 0


def test_set():
    m = Matrix(2,2)
    m[1, 1] = 1
    assert m[1, 1] == 1

@pytest.mark.parametrize(
    'm1,m2,f',
    [
        (
            Matrix(2, 2, [1, 2, 3, 4]),
            Matrix(2, 2, [4, 3, 2, 1]),
            Matrix(2, 2, [5, 5, 5, 5])
        )
    ]
)
def test_add_success(m1, m2, f):

    m3 = m1 + m2

    assert m3 == f


@pytest.mark.parametrize(
    'm1,m2,e',
    [
        (
            Matrix(2, 2),
            Matrix(2, 1),
            ValueError
        ),
    ]
)
def test_add_fail(m1, m2, e):
    with pytest.raises(e):
        m3 = m1 + m2


@pytest.mark.parametrize(
    'm1,m2,f',
    [
        (
            Matrix(1, 2, [2,3]),
            Matrix(2, 1, [2,3]),
            Matrix(1, 1, [13])
        ),
        (
            Matrix(2, 2, [1,2,
                          3,4]),
            Matrix(2, 3, [1,2,3,
                          4,5,6]),
            Matrix(2, 3, [9,12,15,
                          19,26,33])
        ),
    ]
)
def test_mul_success(m1, m2, f):

    m3 = m1 * m2

    assert m3.n_rows == m1.n_rows
    assert m3.n_cols == m2.n_cols

    print(f'm3 = {m3}')
    assert m3 == f


@pytest.mark.parametrize(
    'm1,m2',
    [
        (
            Matrix(1, 2, [2,3]),
            Matrix(1, 2, [2,3]),
        ),
        (
            Matrix(2, 2, [1,2,3,4]),
            Matrix(3, 2, [1,2,3,4,5,6]),
        ),
    ]
)
def test_mul_fail(m1, m2):
    with pytest.raises(ValueError):
        m3 = m1 * m2


@pytest.mark.parametrize(
    'r,c',
    [
        (1,1),
        (1,3),
        (2,3),
        (6,3),
    ]
)
def test_mk_index(r, c):

    m = Matrix(r, c)

    exp_i = 0
    for i in range(r):
        for j in range(c):
            assert m.mk_index(i, j) == exp_i
            exp_i += 1


def test_row_and_col():
    m = Matrix(2, 3, [1, 2, 3,
                      4, 5, 6])
    rows = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    cols = [
        [1, 4],
        [2, 5],
        [3, 6]
    ]

    assert m.n_rows == len(rows)
    assert m.n_cols == len(cols)

    for i, row in enumerate(rows):
        m_row = m.row(i)
        assert len(m_row) == m.n_cols
        assert len(m_row) == len(row)
        assert m_row == row
        # for j in range(len(m_row)):
        #     print(f'm_row[{j}] = {m_row[j]}')
        #     assert m_row[j] == j + 1 + i * (m.n_cols)

    for j, col in enumerate(cols):
        m_col = m.col(j)
        assert len(m_col) == m.n_rows
        assert len(m_col) == len(col)
        assert m_col == col
#        for i in range(len(m_col)):
#            print(f'm_col[{i}] = {m_col[i]}')
#            assert m_col[i] == i * m.n_cols + j + 1

