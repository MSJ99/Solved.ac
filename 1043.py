N, M = map(int, input().split())
L = list(map(int, input().split()))
Tnum = L[0]
L.pop(0)

Tset = set()
if Tnum != 0:
    for item in L:
        Tset.add(item)

Plist = []
for i in range(M):
    PL = list(map(int, input().split()))
    Pnum = PL[0]
    PL.pop(0)

    Pset = set()
    if Pnum != 0:
        for item in PL:
            Pset.add(item)

    Plist.append(Pset)

for j in range(len(Plist)):
    for party in Plist:
        if party.isdisjoint(Tset) == False:
            Tset = Tset | party

result = []
for party in Plist:
    if party.isdisjoint(Tset) == True:
        result.append(party)

print(len(result))
