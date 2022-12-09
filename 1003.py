T = int(input())
Tcase = []
for i in range(T):
    Tcase.append(int(input()))

for j in Tcase:
    if j == 0:
        print(1, 0)
    elif j == 1:
        print(0, 1)
    else:
        array = [(0, 0)] * (j+1)
        array[0] = (1, 0)
        array[1] = (0, 1)
        for k in range(2, j+1):
            array[k] = (array[k-1][0]+array[k-2][0],
                        array[k-1][1]+array[k-2][1])
        print(array[j][0], array[j][1])
