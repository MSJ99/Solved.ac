import sys
from collections import defaultdict

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    dic_1 = defaultdict(str)
    dic_2 = defaultdict(int)
    ans = []
    for i in range(1, N+1):
        pocketmon = sys.stdin.readline().strip()
        dic_1[i] = pocketmon
        dic_2[pocketmon] = i
    for _ in range(M):
        question = sys.stdin.readline().strip()
        try:
            ans.append(dic_1[int(question)])
        except:
            ans.append(dic_2[question])

    for x in ans:
        print(x)
