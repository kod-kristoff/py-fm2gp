# from fm2gp.util import is_odd, half
def half(n: int) -> int:
    return n >> 1


def is_odd(n: int) -> bool:
    return (n & 0x01)


def power_accumulate(r, a, n: int, op):
    if n == 0:
        return r
    while True:
        if n & 0x1:
            r = op(r, a)
            if n == 1:
                return r
        n = n >> 1
        a = op(a, a)


def power_semigroup(x, n: int, op):
    assert n > 0
    while not (n & 0x1):
        print(f"n = {n}, x = {x}")
        x = op(x, x)
        n = n >> 1
    if n == 1:
        return x
    return power_accumulate(x, op(x, x), half(n - 1), op)


if __name__ == "__main__":
    from operator import add
    print(f"r = {power_accumulate(0, 2, 2, add)}")
    print(f"power(3, 6, add) = {power_semigroup(3,6,add)}")
