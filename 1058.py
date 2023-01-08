import sys
from collections import deque


def BFS(num):
    visited = [False] * N
    queue = deque()
    queue.append(num)
    visited[num] = True
    result = 0

    this = queue.popleft()
    for i in range(len(graph[this])):
        if graph[this][i] == 'Y' and visited[i] == False:
            queue.append(i)
            visited[i] = True
            result += 1

    while len(queue) != 0:
        this = queue.popleft()
        for i in range(len(graph[this])):
            if graph[this][i] == 'Y' and visited[i] == False:
                visited[i] = True
                result += 1

    return result


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    graph = []
    result = []
    for _ in range(N):
        friends = sys.stdin.readline().strip()
        graph.append(friends)
    for i in range(N):
        result.append(BFS(i))
    print(max(result))

# 1  2   -> 2, 3
# 2  1 3 -> 1, 3, 4
# 3  2 4 -> 2, 4, 1, 5
# 4  3 5 ->
# 5  4   ->
