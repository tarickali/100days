import math


def sieve(N: int) -> list[int]:
    # Boolean list of numbers 0 to N, True -> prime, False -> composite
    A = [True] * (N + 1)

    # The terminal integer for the outer-loop
    m = int(math.sqrt(N))
    for i in range(2, m + 1):
        # If i is a composite, then continue
        if not A[i]:
            continue
        # Start from j = i^2 to N incrementing by i and mark each j as composite
        j = i**2
        while j <= N:
            A[j] = False
            j += i

    # Filter the primes from A and return
    primes = [i for i in range(2, N + 1) if A[i]]
    return primes


if __name__ == "__main__":
    # A few tests
    assert sieve(5) == [2, 3, 5]
    assert sieve(13) == [2, 3, 5, 7, 11, 13]
    assert sieve(20) == [2, 3, 5, 7, 11, 13, 17, 19]
