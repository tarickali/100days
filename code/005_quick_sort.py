import random


def quick_sort(A: list[int]) -> list[int]:
    # The partition subroutine
    def partition(l: int, r: int):
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
    def recurse(l: int, r: int):
        # Base case: <= 1 element in [l, r)
        if r - l <= 1:
            return
        # Partition the elements of A in [l, r) and get the pivot's final index
        p = partition(l, r)

        # Recursively sort the elements of A in [l, p) and [p+1, r)
        recurse(l, p)
        recurse(p + 1, r)

    # The main recursive call on all elements of A
    recurse(0, len(A))

    return A


if __name__ == "__main__":
    # A few tests
    a = 0
    b = 100
    n = 100
    for _ in range(5):
        A = [random.randint(a, b) for _ in range(n)]
        assert quick_sort(A) == sorted(A)
