import sys
import math

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


result = 0
N = int(sys.stdin.readline())
inputNums = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    if isPrime(inputNums[i]):
        result += 1

print(result)
