import random


def reduction(A: list[int], k: int) -> int:
    A = sorted(A)
    return A[k - 1]


def quickselect(A: list[int], k: int) -> int:
    # The partition subroutine
    def partition(l: int, r: int) -> int:
        # Randomly select a pivot index p from A in [l, r) and
        # set key as A[p]
        p = random.randrange(l, r)
        key = A[p]

        # Swap A[l] and A[p] which simplifies the main-loop
        A[l], A[p] = A[p], A[l]

        # Set the boundary between elements < A[p] and > A[p] to l
        k = l

        # The main-loop
        for i in range(l + 1, r):
            # If A[i] < key then swap A[i] and A[k] and increment the
            # boundary k by 1
            if A[i] < key:
                k += 1
                A[i], A[k] = A[k], A[i]

        # Swap A[l] (the pivot element) with A[k], placing the pivot in
        # its sorted position
        A[l], A[k] = A[k], A[l]

        # Return the index the pivot element was placed in to be used
        # for later recursions
        return k

    # The recursion subroutine
    def recurse(l: int, r: int) -> int:
        # Base case: <= 1 element in [l, r), so return A[l]
        if r - l <= 1:
            return A[l]
        # Partition the elements of A in [l, r) and get the pivot's final index
        p = partition(l, r)

        # If the pivot element is the kth order-statistic return A[p]
        if p + 1 == k:
            return A[p]
        # Recursively search for k in [l, p) and [p+1, r) appropriately
        elif p + 1 > k:
            return recurse(l, p)
        else:
            return recurse(p + 1, r)

    # The main recursive call on all elements of A
    return recurse(0, len(A))


if __name__ == "__main__":
    # A few tests
    n = 100
    A = list(range(n))
    for _ in range(5):
        random.shuffle(A)
        k = random.randint(1, n)
        assert reduction(A, k) == quickselect(A, k)
