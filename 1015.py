import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    elem = list(map(int, sys.stdin.readline().split()))
    A = {}
    for i in range(N):
        A[i] = elem[i]
    A = sorted(A.items(), key=lambda x: x[1])
    P = {}
    for i in range(N):
        P[i] = A[i][0]

    result = dict(zip(P.values(), P.keys()))
    for i in range(N):
        print(result[i], end=' ')
