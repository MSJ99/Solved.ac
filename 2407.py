import sys
from fractions import Fraction


def combinations(n, m):
    if m > n-m:
        return combinations(n, n-m)
    else:
        res = 1
        for i in range(m):
            res *= n-i
        for i in range(1, m+1):
            res = Fraction(res, i)
    return res


if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().split())
    print(combinations(n, m))
