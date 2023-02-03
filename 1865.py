import sys


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    graph = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(0)
            else:
                row.append(1e9)
        graph.append(row)
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        if graph[a-1][b-1] > c:
            graph[a-1][b-1] = c

    res = graph[:]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if res[i][k] + res[k][j] < res[i][j]:
                    res[i][j] = res[i][k] + res[k][j]

    for i in range(n):
        for j in range(n):
            if res[i][j] == 1e9:
                res[i][j] = 0

    for i in range(n):
        for j in range(n):
            print(res[i][j], end=" ")
        print()
