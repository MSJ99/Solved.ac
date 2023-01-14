import sys
from collections import deque


if __name__ == "__main__":
    word = list(sys.stdin.readline().strip())

    while 1:
        q1 = deque()
        q2 = deque()
        idx = int(len(word) / 2)

        for i in range(idx):
            q1.append(word[i])
        for i in range(1, idx+1):
            q2.append(word[-i])

        boolean = True
        for i in range(idx):
            q1Pop = q1.popleft()
            q2Pop = q2.popleft()
            if q1Pop != q2Pop:
                if q1Pop != '*' and q2Pop != '*':
                    boolean = False
                    break

        if boolean == False:
            word.append('*')
        else:
            break

    print(len(word))
