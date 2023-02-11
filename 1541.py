import sys
from collections import deque

if __name__ == "__main__":
    Input = list(sys.stdin.readline().strip())
    equation = deque()
    digit = -1
    value = 0

    for i in reversed(range(len(Input))):
        if Input[i] == '+':
            equation.appendleft(value)
            equation.appendleft('+')
            digit = -1
            value = 0
        elif Input[i] == '-':
            equation.appendleft(value)
            equation.appendleft('-')
            digit = -1
            value = 0
        else:
            digit += 1
            value += int(Input[i]) * (10 ** digit)
            if i == 0:
                equation.appendleft(value)

    if len(equation) == 1:
        print(equation.popleft())
    elif len(equation) == 3:
        left = equation.popleft()
        if equation.popleft() == '+':
            print(left + equation.popleft())
        else:
            print(left - equation.popleft())

    else:
        temp = 0
        total = equation.popleft()
        previousSign = equation.popleft()
        while equation:
            now = equation.popleft()
            if type(now) is int:
                if previousSign == '+':
                    total += now
                else:
                    temp += now
                    if len(equation) == 0:
                        total -= temp

            else:
                if previousSign == '-' and now == '-':
                    total -= temp
                    temp = 0
                elif previousSign == '+' and now == '-':
                    previousSign = '-'
        print(total)
