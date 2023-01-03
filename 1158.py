import sys


if __name__ == "__main__":
    N, K = map(int, sys.stdin.readline().split())
    lst = [0] * N
    result = []
    for i in range(N):
        lst[i] = i+1

    idx = 0
    while len(lst) != 0:
        idx += K-1
        idx %= len(lst)
        target = lst[idx]
        result.append(target)
        lst.remove(target)

    print("<" + ", ".join(list(map(str, result))) + ">")
