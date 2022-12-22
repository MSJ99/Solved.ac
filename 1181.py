import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    lst = []

    for i in range(N):
        lst.append(sys.stdin.readline().strip())
    set_lst = set(lst)
    lst = list(set_lst)
    lst.sort()
    lst.sort(key=len)

    for i in lst:
        print(i)
