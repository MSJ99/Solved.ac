import sys
import heapq


if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())
    INF = int(1e9)
    cost = [INF] * (V+1)
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))

    queue = []
    heapq.heappush(queue, (0, K))
    cost[K] = 0

    while len(queue) != 0:
        val, node = heapq.heappop(queue)
        if cost[node] < val:
            continue
        for x in graph[node]:
            costSum = cost[node] + x[1]
            if costSum < cost[x[0]]:
                cost[x[0]] = costSum
                heapq.heappush(queue, (costSum, x[0]))

    for i in range(1, V+1):
        if cost[i] == INF:
            print("INF")
        else:
            print(cost[i])
