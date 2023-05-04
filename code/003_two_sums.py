# # Brute-force algorithm
def two_sum_brute_force(A: list[int], t: int) -> tuple[int, int] | None:
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] + A[j] == t:
                return (i, j)
    return None


# Slightly inefficient algorithm
def two_sum_v0(A: list[int], t: int) -> tuple[int, int] | None:
    # Preprocessing: a mapping from A[i] to i for each index in A
    T = {x: i for i, x in enumerate(A)}

    # Note: if the values of A are not unique, then T will store the last
    # index of the value, but this does not affect the algorithm.
    # Can you see why?

    for i, x in enumerate(A):
        # Check if y = t - A[i] is in table with j != i.
        # If so then (i, A[y]) is a solution to the problem.
        y = t - x
        if y in T and T[y] != i:
            return (i, T[y])

    # If no pair was found in the above loop, then no pair exists.
    return None


# Final efficient algorithm
def two_sum(A: list[int], t: int) -> tuple[int, int] | None:
    T = {}
    for i, x in enumerate(A):
        y = t - x
        if y in T:
            return (i, T[y])
        T[x] = i
    return None


if __name__ == "__main__":
    # A few tests
    import random

    a, b = 1, 1000
    n = 100

    # Positive examples
    for _ in range(5):
        A = [random.randint(a, b) for _ in range(n)]
        t = sum(random.sample(A, 2))
        sol = two_sum(A, t)
        assert sol != None and A[sol[0]] + A[sol[1]] == t

    # Negative examples
    for _ in range(5):
        A = [random.randint(a, b) for _ in range(n)]
        t = random.choice(list(range(-10, 0)) + list(range(2001, 2010)))
        assert two_sum(A, t) == None
