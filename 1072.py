from decimal import Decimal

X, Y = map(Decimal, input().split())
Z = int((Y/X) * 100)

if (X == Y) or (Z == 99):
    print(-1)
else:
    count = ((100 * (X - Y)) / (99 - Z)) - X
    if count - int(count) == 0:
        print(int(count))
    else:
        print(int(count+1))
