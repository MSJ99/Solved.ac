import sys


if __name__ == "__main__":
    N, L = map(int, sys.stdin.readline().split())
    loc = list(map(int, sys.stdin.readline().split()))

    loc.sort()
    cnt = 1
    d = 0
    for i in range(1, N):
        d += abs(loc[i] - loc[i - 1])
        if L > d:
            continue
        else:
            cnt += 1
            d = 0
    print(cnt)
