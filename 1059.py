import sys


if __name__ == "__main__":
    L = int(sys.stdin.readline())
    S = sorted(list(map(int, sys.stdin.readline().split())))
    n = int(sys.stdin.readline())

    if n in S:
        print(0)
    else:
        MIN = 0
        MAX = 1001

        for x in S:
            if x > n:
                MAX = x
                break
        MAX -= 1

        for x in S:
            if x < n:
                MIN = x
        MIN += 1

        print((n - MIN) + (MAX - n) + (n - MIN)*(MAX - n))
