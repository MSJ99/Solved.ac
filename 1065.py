import sys


def IsHanSoo(num: int):
    digit = len(str(num))
    if digit <= 2:
        return True
    else:
        value = []
        for i in range(digit):
            value.append(int(str(num)[i]))
        d = value[0] - value[1]
        for i in range(2, digit):
            if value[i-1] - value[i] != d:
                return False
        return True


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    result = []
    for i in range(1, N+1):
        if IsHanSoo(i):
            result.append(i)
    print(len(result))
