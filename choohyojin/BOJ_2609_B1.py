# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.
N, M = map(int, input().split())

little = min(N, M)

for i in range(little, 0, -1):
    if N % i == 0 and M % i == 0:
        print(i)
        break

nMul = mMul = 1
while True:
    nResult = N * nMul
    mResult = M * mMul
    if nResult == mResult:
        print(nResult)
        break
    elif nResult > mResult:
        mMul += 1
    else:
        nMul += 1