import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    tri = []
    for _ in range(N):
        tri.append(list(map(int, sys.stdin.readline().split())))
    cnt = N
    while cnt != 1:
        for i in range(cnt - 1):  # 가로
            tri[cnt-2][i] = max(tri[cnt-2][i] + tri[cnt-1]
                                [i], tri[cnt-2][i] + tri[cnt-1][i+1])
        cnt -= 1

    print(tri[0])
