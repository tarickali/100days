def karatsuba(x: int, y: int) -> int:
    # Determine the number of digits for x and y
    nx = len(str(x))
    ny = len(str(y))

    # If either x or y has only one digit, then execute the base case
    if nx == 1 or ny == 1:
        return x * y

    # Get the maximum number of digits between x and y
    n = max(nx, ny) // 2

    # For x get x0 and x1 such that x = 10^n * x0 + x1
    x0 = x // (10**n)
    x1 = x % (10**n)

    # For y get y0 and y1 such that y = 10^n * y0 + y1
    y0 = y // (10**n)
    y1 = y % (10**n)

    # Perform the divide step of the algorithm for the three recursive calls
    z0 = karatsuba(x0, y0)
    z1 = karatsuba(x1, y1)
    z2 = karatsuba(x0 + x1, y0 + y1)

    # Perform the conquer step of the algorithm joining z0, z1, z2
    return 10 ** (2 * n) * z0 + 10 ** (n) * (z2 - z1 - z0) + z1


if __name__ == "__main__":
    # A few tests
    import random

    a, b = 1, 1000000000
    for _ in range(10):
        x = random.randint(a, b)
        y = random.randint(a, b)
        assert x * y == karatsuba(x, y)
