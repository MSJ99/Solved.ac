import sys


def countMatch(a: list, b: list):
    cnt: int = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            if a[i] != ' ':
                cnt += 1
    return cnt


if __name__ == "__main__":
    A, B = sys.stdin.readline().split()
    A = list(A)
    B = list(B)

    if len(A) == len(B):
        print(countMatch(A, B))
    else:
        result = []
        for i in range(len(B)-len(A)+1):
            edit = A[:]
            for x in range(i):
                edit.insert(0, ' ')
            for y in range(len(B)-len(A)-i):
                edit.append(' ')
            result.append(countMatch(edit, B))
        print(min(result))
