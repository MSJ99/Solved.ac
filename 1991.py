import sys
from collections import defaultdict


def PREORDER(val):
    if val != '.':
        print(val, end='')
        PREORDER(graph[val][0])
        PREORDER(graph[val][1])


def INORDER(val):
    if val != '.':
        INORDER(graph[val][0])
        print(val, end='')
        INORDER(graph[val][1])


def POSTORDER(val):
    if val != '.':
        POSTORDER(graph[val][0])
        POSTORDER(graph[val][1])
        print(val, end='')


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    graph = defaultdict()
    for _ in range(N):
        node = list(sys.stdin.readline().split())
        graph[node[0]] = (node[1], node[2])
    PREORDER('A')
    print()
    INORDER('A')
    print()
    POSTORDER('A')
