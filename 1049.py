import sys

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    price_six: list = []
    price_one: list = []

    for i in range(M):
        six, one = map(int, sys.stdin.readline().split())
        price_six.append(six)
        price_one.append(one)

    minOfSix = min(price_six)
    minOfOne = min(price_one)

    u: int = minOfSix * (N//6) + minOfOne * (N % 6)
    v: int = minOfSix * ((N//6)+1)
    w: int = minOfOne * N

    print(min(u, v, w))
