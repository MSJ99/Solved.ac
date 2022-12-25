import sys


def move(lst: list, orderName: str):
    if orderName == 'R':
        if lst[0] == 'A':
            lst[0] = 'B'
        elif lst[0] == 'B':
            lst[0] = 'C'
        elif lst[0] == 'C':
            lst[0] = 'D'
        elif lst[0] == 'D':
            lst[0] = 'E'
        elif lst[0] == 'E':
            lst[0] = 'F'
        elif lst[0] == 'F':
            lst[0] = 'G'
        elif lst[0] == 'G':
            lst[0] = 'H'
    elif orderName == 'L':
        if lst[0] == 'B':
            lst[0] = 'A'
        elif lst[0] == 'C':
            lst[0] = 'B'
        elif lst[0] == 'D':
            lst[0] = 'C'
        elif lst[0] == 'E':
            lst[0] = 'D'
        elif lst[0] == 'F':
            lst[0] = 'E'
        elif lst[0] == 'G':
            lst[0] = 'F'
        elif lst[0] == 'H':
            lst[0] = 'G'
    elif orderName == 'B':
        if lst[1] != 1:
            lst[1] -= 1
    elif orderName == 'T':
        if lst[1] != 8:
            lst[1] += 1
    elif orderName == "RT":
        if lst[0] == 'A' and lst[1] != 8:
            lst[0] = 'B'
            lst[1] += 1
        elif lst[0] == 'B' and lst[1] != 8:
            lst[0] = 'C'
            lst[1] += 1
        elif lst[0] == 'C' and lst[1] != 8:
            lst[0] = 'D'
            lst[1] += 1
        elif lst[0] == 'D' and lst[1] != 8:
            lst[0] = 'E'
            lst[1] += 1
        elif lst[0] == 'E' and lst[1] != 8:
            lst[0] = 'F'
            lst[1] += 1
        elif lst[0] == 'F' and lst[1] != 8:
            lst[0] = 'G'
            lst[1] += 1
        elif lst[0] == 'G' and lst[1] != 8:
            lst[0] = 'H'
            lst[1] += 1
    elif orderName == "LT":
        if lst[0] == 'B' and lst[1] != 8:
            lst[0] = 'A'
            lst[1] += 1
        elif lst[0] == 'C' and lst[1] != 8:
            lst[0] = 'B'
            lst[1] += 1
        elif lst[0] == 'D' and lst[1] != 8:
            lst[0] = 'C'
            lst[1] += 1
        elif lst[0] == 'E' and lst[1] != 8:
            lst[0] = 'D'
            lst[1] += 1
        elif lst[0] == 'F' and lst[1] != 8:
            lst[0] = 'E'
            lst[1] += 1
        elif lst[0] == 'G' and lst[1] != 8:
            lst[0] = 'F'
            lst[1] += 1
        elif lst[0] == 'H' and lst[1] != 8:
            lst[0] = 'G'
            lst[1] += 1
    elif orderName == "RB":
        if lst[0] == 'A' and lst[1] != 1:
            lst[0] = 'B'
            lst[1] -= 1
        elif lst[0] == 'B' and lst[1] != 1:
            lst[0] = 'C'
            lst[1] -= 1
        elif lst[0] == 'C' and lst[1] != 1:
            lst[0] = 'D'
            lst[1] -= 1
        elif lst[0] == 'D' and lst[1] != 1:
            lst[0] = 'E'
            lst[1] -= 1
        elif lst[0] == 'E' and lst[1] != 1:
            lst[0] = 'F'
            lst[1] -= 1
        elif lst[0] == 'F' and lst[1] != 1:
            lst[0] = 'G'
            lst[1] -= 1
        elif lst[0] == 'G' and lst[1] != 1:
            lst[0] = 'H'
            lst[1] -= 1
    elif orderName == "LB":
        if lst[0] == 'B' and lst[1] != 1:
            lst[0] = 'A'
            lst[1] -= 1
        elif lst[0] == 'C' and lst[1] != 1:
            lst[0] = 'B'
            lst[1] -= 1
        elif lst[0] == 'D' and lst[1] != 1:
            lst[0] = 'C'
            lst[1] -= 1
        elif lst[0] == 'E' and lst[1] != 1:
            lst[0] = 'D'
            lst[1] -= 1
        elif lst[0] == 'F' and lst[1] != 1:
            lst[0] = 'E'
            lst[1] -= 1
        elif lst[0] == 'G' and lst[1] != 1:
            lst[0] = 'F'
            lst[1] -= 1
        elif lst[0] == 'H' and lst[1] != 1:
            lst[0] = 'G'
            lst[1] -= 1

    return lst


if __name__ == "__main__":
    K, R, N = sys.stdin.readline().split()
    Kloc = list(K.strip())
    Kloc[1] = int(Kloc[1])
    Rloc = list(R.strip())
    Rloc[1] = int(Rloc[1])

    N = int(N)

    for i in range(N):
        order = sys.stdin.readline().strip()
        tempK = Kloc[:]
        tempR = Rloc[:]
        if move(tempK, order) != Rloc or Rloc != move(tempR, order):
            Kloc = move(Kloc, order)
            if Kloc == Rloc:
                Rloc = move(Rloc, order)

    print(Kloc[0], Kloc[1], sep="")
    print(Rloc[0], Rloc[1], sep="")
