import sys
from collections import defaultdict


def topDown(n, p, q):
    if A[n] != 0:
        return A[n]
    A[n] = topDown(n//p, p, q) + topDown(n//q, p, q)
    return A[n]


if __name__ == "__main__":
    N, P, Q = map(int, sys.stdin.readline().split())
    A = defaultdict(int)
    A[0] = 1
    print(topDown(N, P, Q))
