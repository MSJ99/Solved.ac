import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    jail = [[1, 1, 1]] * N
    for i in range(1, N):
        jail[i] = [sum(jail[i-1]) % 9901, (sum(jail[i-1]) - jail[i-1][1]) %
                   9901, (sum(jail[i-1]) - jail[i-1][2]) % 9901]
    print(sum(jail[N-1]) % 9901)
