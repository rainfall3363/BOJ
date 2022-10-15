import sys

def isDoomsDay(num):
    subject = str(num)
    if "666" in subject:
        return True
    else:
        return False


N = int(sys.stdin.readline())
doomsdayCnt = 1
it = 666

while doomsdayCnt < N:
    it += 1
    if isDoomsDay(it):
        doomsdayCnt += 1
    
print(it)