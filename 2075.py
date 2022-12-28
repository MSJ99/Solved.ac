import sys
import heapq

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    heap = []
    for _ in range(N):
        row = map(int, sys.stdin.readline().split())
        for item in row:
            heapq.heappush(heap, item)
            if len(heap) > N:
                heapq.heappop(heap)

    for i in range(N):
        heap[i] = -heap[i]
    heapq.heapify(heap)

    for _ in range(N-1):
        heapq.heappop(heap)
    print(-heapq.heappop(heap))
