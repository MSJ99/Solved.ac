import sys
from itertools import permutations


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    Num = sorted(list(map(int, sys.stdin.readline().split())))
    seq = list(permutations(Num, M))
    for x in seq:
        for y in x:
            print(y, end=" ")
        print()
