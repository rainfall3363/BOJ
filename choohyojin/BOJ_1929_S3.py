import sys

def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

M, N = map(int, sys.stdin.readline().split())

for i in range(M, N + 1):
    if isPrime(i):
        print(i)
