import sys
from itertools import combinations


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    nums = []
    for i in range(N):
        nums.append(i+1)
    res = list(combinations(nums, M))
    for x in res:
        for y in x:
            print(y, end=" ")
        print()
