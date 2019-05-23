from fm2gp.primes import mark_sieve


def test_mark_sieve():
    n = 20
    lst = [True for _ in range(n)]
    mark_sieve(lst, 3, 3)

    for i, v in enumerate(lst):
        value = 2 * i + 3
        print('{i} -> {value}: {v}')
        if i > 0 and value % 3 == 0:
            assert v == False
        else:
            assert v == True

