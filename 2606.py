import sys
from collections import deque


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        graph[A].append(B)
        graph[B].append(A)

    visited = [False] * (N+1)
    q = deque()
    q.append(1)
    visited[1] = True
    while q:
        now = q.popleft()
        for x in graph[now]:
            if visited[x] == False:
                q.append(x)
                visited[x] = True

    cnt = 0
    for i in range(2, N+1):
        if visited[i] == True:
            cnt += 1
    print(cnt)
