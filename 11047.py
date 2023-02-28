import sys
from collections import deque

if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    coin = deque()
    for _ in range(N):
        Ai = int(sys.stdin.readline())
        if Ai <= K:
            coin.append(Ai)

    cnt = 0
    while coin:
        if K == 0:
            break
        now = coin.pop()
        if now <= K:
            while now <= K:
                K -= now
                cnt += 1

    print(cnt)
