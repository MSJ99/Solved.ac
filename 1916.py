import sys
import heapq
from collections import deque


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    M = int(sys.stdin.readline())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
    start, end = map(int, sys.stdin.readline().split())

    distance = [1e9] * (N+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, node = heapq.heappop(q)
        if distance[node] < cost:
            continue

        for next in graph[node]:
            newcost = distance[node] + next[1]
            if newcost < distance[next[0]]:
                heapq.heappush(q, (newcost, next[0]))
                distance[next[0]] = newcost

    print(distance[end])
