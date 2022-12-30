import sys

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    if N % 4 == 0 and N % 100 != 0:
        print(1)
    elif N % 400 == 0:
        print(1)
    else:
        print(0)
