import sys

answer = []
lines = []

while True:
    lines = list(map(int, sys.stdin.readline().split(' ')))
    lines.sort()
    
    if lines[0] == 0:
        break
    
    if lines[0] ** 2 + lines[1] ** 2 == lines[2] ** 2:
        answer.append("right")
    else:
        answer.append("wrong")
        
for i in range(len(answer)):
    print(answer[i])
