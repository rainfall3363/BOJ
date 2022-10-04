import sys
N = int(sys.stdin.readline())
arrN = list(map(int, sys.stdin.readline().split()))
arrN.sort()
M = int(sys.stdin.readline())
arrM = list(map(int, sys.stdin.readline().split()))
copiedArrM = list(arrM)
arrM.sort()

nIdx = 0
mIdx = 0
matchSet = set()
while nIdx < N and mIdx < M:
    if arrN[nIdx] < arrM[mIdx]:
        nIdx += 1
    elif arrN[nIdx] == arrM[mIdx]:
        matchSet.add(arrM[mIdx])
        nIdx += 1
        mIdx += 1
    else:
        mIdx += 1

for i in range(len(copiedArrM)):
    if copiedArrM[i] in matchSet:
        print(1)
    else:
        print(0)
        