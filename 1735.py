import sys


if __name__ == "__main__":
    A, B = map(int, sys.stdin.readline().split())
    C, D = map(int, sys.stdin.readline().split())

    numerator = A*D + B*C
    denominator = B*D

    if numerator >= denominator:
        big = numerator
        small = denominator
    else:
        big = denominator
        small = numerator

    while 1:
        r = big - (small * (big // small))
        if r == 0:
            break
        big = small
        small = r

    print(int(numerator/small), int(denominator/small))
