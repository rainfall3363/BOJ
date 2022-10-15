import sys
from collections import deque

N = int(sys.stdin.readline())
pairs = [sys.stdin.readline().strip() for i in range(N)]

for i in range(len(pairs)):
    flag = True
    dq = deque(pairs[i])
    leftCnt = 0
    
    for j in range(len(pairs[i])):
        popped = dq.popleft()
        if popped == "(":
            leftCnt += 1
        elif popped == ")":
            if leftCnt == 0:
                flag = False
                break
            else:
                leftCnt -= 1
    
    if flag and leftCnt == 0:
        print("YES")
    else:
        print("NO")
