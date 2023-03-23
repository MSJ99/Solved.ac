import sys


if __name__ == "__main__":
    N = int(sys.stdin.readline())
    b = []
    height = list(map(int, sys.stdin.readline().split()))
    for x in height:
        b.append(x)

    res = []
    for i in range(N):
        cnt = 0
        for j in range(N):
            if i == j:
                continue
            d = (b[i]-b[j])/(i-j)
            see = True
            for k in range(min(i, j), max(i, j)+1):
                if k == i or k == j:
                    continue
                if b[k] >= d*(k-i)+b[i]:
                    see = False
                    break
            if see:
                cnt += 1
        res.append(cnt)
    print(max(res))
