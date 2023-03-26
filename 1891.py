import sys
from collections import deque


def NumToIdx(d, num: deque, row, col):
    if d == 0:
        return (row, col)
    else:
        now = num.popleft()
        if now == 1:
            col += 2**(d-1)
        elif now == 3:
            row += 2**(d-1)
        elif now == 4:
            row += 2**(d-1)
            col += 2**(d-1)

        return NumToIdx(d - 1, num, row, col)


def IdxToNum(d, row, col):
    if d == 0:
        return

    if row <= 2**(d-1):
        if col <= 2**(d-1):
            print(2, end="")
        else:
            col -= 2**(d-1)
            print(1, end="")
    else:
        row -= 2**(d-1)
        if col <= 2**(d-1):
            print(3, end="")
        else:
            col -= 2**(d-1)
            print(4, end="")

    return IdxToNum(d-1, row, col)


if __name__ == "__main__":
    d, num = map(int, sys.stdin.readline().split())
    x, y = map(int, sys.stdin.readline().split())

    q = deque()
    for i in str(num):
        q.append(int(i))

    idx = NumToIdx(d, q, 1, 1)
    if x + idx[1] < 1 or x + idx[1] > 2**d:
        print(-1)
    elif idx[0] - y < 1 or idx[0] - y > 2**d:
        print(-1)
    else:
        IdxToNum(d, idx[0] - y, idx[1] + x)


#   222 221 212 211 122 121 112 111
#   223 224 213 214 123 124 113 114
#   232 231 242 241 132 131 142 141
#   233 234 243 244 133 134 143 144
#   322 321 312 311 422 421 412 411
#   323 324 313 314 423 424 413 414
#   332 331 342 341 432 431 442 441
#   333 334 343 344 433 434 443 444
