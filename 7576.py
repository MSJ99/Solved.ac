import sys
from collections import deque


def tsum(t1: tuple, t2: tuple):
    return (t1[0] + t2[0], t1[1] + t2[1])


def BFS(graph, row, col):
    visited = [[False for _ in range(col)] for _ in range(row)]
    q = deque()
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1:
                q.append((i, j))
    dayover = -1
    q.append(dayover)

    move = {(0, 1), (1, 0), (-1, 0), (0, -1)}

    cnt = 0
    while q:
        now = q.popleft()
        if now == dayover:
            if q:
                cnt += 1
                q.append(dayover)
            else:
                break
        else:
            for x in move:
                next = tsum(now, x)
                if next[0] < 0 or next[0] >= row:
                    continue
                if next[1] < 0 or next[1] >= col:
                    continue
                if graph[next[0]][next[1]] == 0:
                    if visited[next[0]][next[1]] == False:
                        q.append(next)
                        visited[next[0]][next[1]] = True
                        graph[next[0]][next[1]] = 1

    ripen = True
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 0:
                ripen = False

    if ripen:
        return cnt
    else:
        return -1


if __name__ == "__main__":
    M, N = map(int, sys.stdin.readline().split())
    box = []
    for _ in range(N):
        box.append(list(map(int, sys.stdin.readline().split())))

    ripen = True
    for i in range(N):
        if not ripen:
            break
        for j in range(M):
            if box[i][j] == 0:
                ripen = False
                break

    if ripen:
        print(0)
    else:
        print(BFS(box, N, M))
