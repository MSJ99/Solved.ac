import sys
from collections import defaultdict

if __name__ == "__main__":
    Name = defaultdict(int)

    engName = sys.stdin.readline().strip()
    N = int(sys.stdin.readline())
    for _ in range(N):
        teamName = sys.stdin.readline().strip()
        L = 0
        O = 0
        V = 0
        E = 0
        for i in range(len(engName)):
            if engName[i] == 'L':
                L += 1
            elif engName[i] == 'O':
                O += 1
            elif engName[i] == 'V':
                V += 1
            elif engName[i] == 'E':
                E += 1
        for i in range(len(teamName)):
            if teamName[i] == 'L':
                L += 1
            elif teamName[i] == 'O':
                O += 1
            elif teamName[i] == 'V':
                V += 1
            elif teamName[i] == 'E':
                E += 1

        Name[teamName] = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
    print(sorted(k for k, v in Name.items() if max(Name.values()) == v)[0])
