import sys
import heapq


if __name__ == "__main__":
    N, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(E):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    v1, v2 = map(int, sys.stdin.readline().split())

    inf = 1e9

    def dijkstra(start, end):
        q = []
        distance = [inf for _ in range(N + 1)]
        distance[start] = 0
        heapq.heappush(q, (0, start))

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for next in graph[now]:
                cost = distance[now] + next[1]
                if cost < distance[next[0]]:
                    distance[next[0]] = cost
                    heapq.heappush(q, (cost, next[0]))

        return distance[end]

    ans1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
    ans2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)
    if ans1 >= inf and ans2 >= inf:
        print(-1)
    else:
        print(min(ans1, ans2))
