import sys
import heapq


def Dijkstra(graph: list, X: int):
    distance = [1e9] * (N+1)
    distance[X] = 0
    q = []
    heapq.heappush(q, (0, X))

    while q:
        cost, now = heapq.heappop(q)
        for x in graph[now]:
            next = x[0]
            nextC = cost + x[1]
            if distance[next] < nextC:
                continue
            distance[next] = nextC
            heapq.heappush(q, (nextC, next))

    return distance


if __name__ == "__main__":
    N, M, X = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end, T = map(int, sys.stdin.readline().split())
        graph[start].append((end, T))

    res = [0] * (N+1)

    # X -> 각자의 집 계산
    XtoH = Dijkstra(graph, X)
    for i in range(1, N+1):
        res[i] += XtoH[i]

    # 각자의 집 -> X 계산
    for i in range(1, N+1):
        if i == X:
            continue
        HtoX = Dijkstra(graph, i)
        res[i] += HtoX[X]

    print(max(res))
