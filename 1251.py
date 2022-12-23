import sys

if __name__ == "__main__":
    word = sys.stdin.readline().strip()
    word = list(word)
    # [m,o,b,i,t,e,l]: 7개
    result = []
    for i in range(len(word)-2):
        s1 = word[:i+1]
        for j in range(i+1, len(word)-1):
            s2 = word[i+1:j+1]
            s3 = word[j+1:]
            result.append(s1[::-1]+s2[::-1]+s3[::-1])

    result.sort()
    for ch in result[0]:
        print(ch, end="")
