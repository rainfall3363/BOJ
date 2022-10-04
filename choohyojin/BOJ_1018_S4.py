def numOfDiffLetters(y, x, inputBoard, bwBoard):
    diff = 0
    for i in range(8):
        for j in range(8):
            if inputBoard[i + y][j + x] != bwBoard[i][j]:
                diff += 1
    
    return diff


n, m = map(int, input().split())
inputBoard = []
for i in range(n):
    inputBoard.append(input())

diff = 64

# 비교할 배열
bwBoard = ['BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB']
wbBoard = ['WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW']

for i in range(n):
    for j in range(m):
        if i + 7 < n and j + 7 < m:
            diff = min(diff, numOfDiffLetters(i, j, inputBoard, bwBoard), numOfDiffLetters(i,j, inputBoard, wbBoard))
        
print(diff)