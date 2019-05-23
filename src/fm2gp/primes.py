
def mark_sieve(arr, first, factor):
    assert first < len(arr)
    arr[first] = False
    while len(arr) - first > factor:
        first = first + factor
        arr[first] = False

