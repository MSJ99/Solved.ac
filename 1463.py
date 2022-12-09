X = int(input())
List = []
List.append(0)
List.append(1)
List.append(1)

while X > 3:
    num = len(List)+1
    newList = []
    if num % 3 == 0:
        val_div3 = List[int(num/3)-1]+1
        newList.append(val_div3)

    if num % 2 == 0:
        val_div2 = List[int(num/2)-1]+1
        newList.append(val_div2)

    val_min1 = List[num-2]+1
    newList.append(val_min1)

    List.append(min(newList))

    if len(List) == X:
        print(List[-1])
        break

if 0 < X < 4:
    print(List[X-1])
