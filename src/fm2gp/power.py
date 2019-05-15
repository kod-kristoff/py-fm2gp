# from fm2gp.util import is_odd, half

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


if __name__ == "__main__":
    from operator import add
    print(f"r = {power_accumulate(0, 2, 2, add)}")
