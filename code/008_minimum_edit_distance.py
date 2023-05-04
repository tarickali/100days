def edit_distance(s: str, t: str, c_s: int = 1, c_d: int = 1, c_i: int = 1) -> int:
    memo = {}

    def recurse(i: int, j: int) -> int:
        # NOTE: we are using 1-based indexing, so base cases are 0, not -1
        # Look up the result if the (i, j) subproblem was previously solved
        if (i, j) in memo:
            return memo[(i, j)]
        if i == 0:  # Base case
            res = j
        elif j == 0:  # Base case
            res = i
        elif s[i - 1] == t[j - 1]:  # Special case when current characters match
            res = recurse(i - 1, j - 1)
        else:  # General recursive case
            res = min(
                c_s + recurse(i - 1, j - 1),
                c_d + recurse(i - 1, j),
                c_i + recurse(i, j - 1),
            )
        # Store the result in memo for quick look-up later
        memo[(i, j)] = res
        return res

    return recurse(len(s), len(t))


if __name__ == "__main__":
    # A few tests
    assert edit_distance("abcde", "abcde") == 0
    assert edit_distance("hello", "world") == 4
    assert edit_distance("agtcctga", "agctcga") == 3
