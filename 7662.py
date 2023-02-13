import sys
import heapq
from collections import defaultdict

if __name__ == "__main__":
    ans = []
    T = int(sys.stdin.readline())
    for _ in range(T):
        minQ = []
        maxQ = []
        dic = defaultdict(int)
        k = int(sys.stdin.readline())
        for _ in range(k):
            order, num = map(str, sys.stdin.readline().split())
            num = int(num)
            if order == 'I':
                dic[num] += 1
                heapq.heappush(minQ, num)
                heapq.heappush(maxQ, -num)
            elif order == 'D':
                if num == 1:
                    while maxQ:
                        M = -heapq.heappop(maxQ)
                        if dic[M] != 0:
                            dic[M] -= 1
                            break
                elif num == -1:
                    while minQ:
                        m = heapq.heappop(minQ)
                        if dic[m] != 0:
                            dic[m] -= 1
                            break
        while maxQ and dic[-maxQ[0]] == 0:
            heapq.heappop(maxQ)
        while minQ and dic[minQ[0]] == 0:
            heapq.heappop(minQ)

        if minQ and maxQ:
            ans.append((-maxQ[0], minQ[0]))
        else:
            ans.append("EMPTY")

    for x in ans:
        if type(x) is tuple:
            for y in x:
                print(y, end=' ')
            print()
        else:
            print(x)
