def determine(lst: list, lenghts: list):
    result: int = 0

    for i in range(len(lst)):
        cnt: int = 0
        char: set = set()

        for j in range(len(lst[i])):
            if lst[i][j] in char:
                if lst[i][j] != lst[i][j-1]:
                    cnt -= 1
            else:
                char.add(lst[i][j])
            cnt += 1

        if cnt == lengths[i]:
            result += 1

    return result


N = int(input())
words: list = []
lengths: list = []
for i in range(N):
    word: str = input()
    words.append(word)
    lengths.append(len(word))

print(determine(words, lengths))
