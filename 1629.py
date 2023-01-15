import sys


def power(a, b, c):
    if b == 1:
        return a % c
    elif b == 2:
        return a * a % c
    else:
        if b % 2 == 1:
            return (power(a, b // 2, c) ** 2) * a % c
        else:
            return (power(a, b // 2, c) ** 2) % c


if __name__ == "__main__":
    A, B, C = map(int, sys.stdin.readline().split())
    print(power(A, B, C))

# 10 ^ 11 % 12 =>
