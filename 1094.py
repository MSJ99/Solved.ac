X = int(input())


def sum(List):
    result = 0
    for item in List:
        result += item
    return result


stick = [64]

while 1:
    if sum(stick) > X:
        stick[stick.index(min(stick))] = min(stick) / 2
        stick.append(min(stick))
        if sum(stick) - min(stick) >= X:
            stick.remove(min(stick))
    elif sum(stick) == X:
        print(len(stick))
        break
