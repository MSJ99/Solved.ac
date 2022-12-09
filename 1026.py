N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0

while len(A) != 0:
    min_A = min(A)
    max_A = max(A)
    min_B = min(B)
    max_B = max(B)

    if min_A * max_B > max_A * min_B:
        result += max_A * min_B
        A.remove(max_A)
        B.remove(min_B)
    else:
        result += min_A * max_B
        A.remove(min_A)
        B.remove(max_B)

print(result)
