import sys


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    graph = []
    for i in range(N):
        row = []
        for j in range(N):
            if i == j:
                row.append(0)
            else:
                row.append(1e9)
        graph.append(row)
    for _ in range(M):
        A, B = map(int, sys.stdin.readline().split())
        graph[A-1][B-1] = 1
        graph[B-1][A-1] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    res = []
    for x in graph:
        sum = 0
        for y in x:
            if y == 1e9:
                continue
            sum += y
        res.append(sum)

    print(res.index(min(res)) + 1)
