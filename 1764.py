import sys


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    Hpeople = set()
    Speople = set()
    for _ in range(N):
        Heard = sys.stdin.readline().strip()
        Hpeople.add(Heard)
    for _ in range(M):
        Seen = sys.stdin.readline().strip()
        Speople.add(Seen)

    result = sorted(list(Hpeople & Speople))
    print(len(result))
    for x in result:
        print(x)
