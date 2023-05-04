def brute_force_search(A: list[int], t: int) -> bool:
    for x in A:
        if x == t:
            return True
    return False


def binary_search_iterative(A: list[int], t: int) -> bool:
    l = 0
    r = len(A)

    # Loop until l >= r, meaning until the subarray is length 0
    while l < r:
        # Find the middle index of the subarray
        m = l + (r - l) // 2
        # If the middle element is the target, then return True
        if A[m] == t:
            return True
        # Otherwise, recurse on the left or right depending on A[m] and t
        elif A[m] < t:
            l = m + 1
        else:
            r = m
    # If t was not found in the main loop then t is not in A
    return False


def binary_search_recursive(A: list[int], t: int) -> bool:
    def recurse(l: int, r: int) -> bool:
        # Base case when l >= r
        if l >= r:
            return A[l] == t
        # Find the middle index of the subarray
        m = l + (r - l) // 2
        # If the middle element is the target, then return True
        if A[m] == t:
            return True
        # Otherwise, recurse on the left or right depending on A[m] and t
        elif A[m] < t:
            return recurse(m + 1, r)
        else:
            return recurse(l, m)

    # The main recursive call
    return recurse(0, len(A))


if __name__ == "__main__":
    # A few tests
    import random

    n = 100
    a, b = 1, 1000
    A = sorted(random.randint(a, b) for _ in range(n))

    # Positive examples
    for _ in range(5):
        t = random.choice(A)
        assert binary_search_iterative(A, t) == binary_search_recursive(A, t) == True

    # Negative examples
    B = sorted(list(set(range(1000)) - set(A)))
    for _ in range(5):
        t = random.choice(B)
        assert binary_search_iterative(A, t) == binary_search_recursive(A, t) == False
