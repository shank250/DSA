
# import sys
# import numpy as np

# MOD = 10**9 + 7
# input = sys.stdin.readline

# def matpow_np(M: np.ndarray, p: int) -> np.ndarray:
#     """Compute M^p mod MOD via binary exponentiation, using NumPy dot."""
#     n = M.shape[0]
#     # Start with identity
#     R = np.eye(n, dtype=np.int64)
#     base = M.copy()
#     while p:
#         if p & 1:
#             # multiply and immediately reduce mod
#             R = (R.dot(base)) % MOD
#         base = (base.dot(base)) % MOD
#         p >>= 1
#     return R

# def main():
#     A, B, C = map(int, input().split())
#     # Edge case: length-1 arrays are just C choices
#     if A == 1:
#         print(C % MOD)
#         return

#     # build the B×B transition matrix
#     M = np.zeros((B, B), dtype=np.int64)
#     # first row = (C-1) everywhere
#     M[0, :] = (C - 1) % MOD
#     # subdiagonal = 1
#     for i in range(1, B):
#         M[i, i-1] = 1

#     # initial dp-vector v1 = [C, 0, 0, …, 0]^T
#     v1 = np.zeros((B,), dtype=np.int64)
#     v1[0] = C % MOD

#     # raise M to the (A-1)-th power
#     MA = matpow_np(M, A-1)

#     # apply to v1
#     vA = (MA.dot(v1)) % MOD

#     # answer = sum of all states
#     print(int(vA.sum() % MOD))

# if __name__ == "__main__":
#     main()

"""
Module: failure_probability

This module provides a function to compute, for each query interval \([\u2113, r]\),
the probability that a binary-search-like pseudocode fails to "find" a uniformly random target
within the interval.  The probabilities are returned modulo \(10^9+7\).
"""

MOD = 10**9 + 7


def failure_probabilities(queries):
    """
    Given a list of queries, where each query is a pair (l, r) of integers with 1 <= l <= r,
    compute for each the failure probability that the following pseudocode does NOT print "Found":

        l0, r0 = l, r
        while l0 < r0:
            mid = (l0 + r0) // 2
            if target < mid:
                r0 = mid - 1
            elif target > mid:
                l0 = mid + 1
            else:
                print("Found")
                break

    The target is assumed uniform over {l, l+1, ..., r}.  The failure probability is
    (# of "bad" targets) / (r - l + 1), returned as p * inv(q) mod MOD.

    Parameters:
        queries (List[Tuple[int,int]]): list of (l, r) intervals.

    Returns:
        List[int]: list of integers where each entry is the failure probability for the
        corresponding query, computed modulo 10^9+7.
    """
    # Compute maximum interval length
    lengths = [r - l + 1 for (l, r) in queries]
    n_max = max(lengths, default=0)

    # Precompute F[n] = number of failing targets (BST leaves) for each n
    F = [0] * (n_max + 1)
    if n_max >= 1:
        F[1] = 1
    for n in range(2, n_max + 1):
        L = (n - 1) // 2
        R = (n - 1) - L
        F[n] = F[L] + F[R]

    # Precompute modular inverses 1..n_max
    inv = [0] * (n_max + 1)
    if n_max >= 1:
        inv[1] = 1
    for i in range(2, n_max + 1):
        inv[i] = MOD - (MOD // i) * inv[MOD % i] % MOD

    # Compute answers
    result = []
    for n in lengths:
        if n <= 0:
            result.append(0)
        else:
            result.append((F[n] * inv[n]) % MOD)
    return result


if __name__ == '__main__':
    # Example usage
    sample_queries = [(2, 9), (10, 10), (10, 12)]
    answers = failure_probabilities(sample_queries)
    print(answers)  # [500000004, 1, 666666672]
