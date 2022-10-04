# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 
# 결과 값은 한 줄에 하나씩 출력한다.

import sys

N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))




for i in range(N):
    print(nums[i])