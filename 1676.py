import sys


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    f = str(factorial(N))

    pointer = -1
    cnt = 0
    while 1:
        if f[pointer] == '0':
            pointer -= 1
            cnt += 1
        else:
            break

    print(cnt)
