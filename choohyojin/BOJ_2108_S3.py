'''
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.
'''
import sys

N = int(sys.stdin.readline())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline().strip()))
 
nums.sort()

numsDict = {}
for i in range(len(nums)):
    if nums[i] in numsDict:
        numsDict[nums[i]] += 1
    else:
        numsDict[nums[i]] = 1

maxValue = max(numsDict.values())
modes = [k for k, v in numsDict.items() if v == maxValue]

mode = 0
if len(modes) > 1:
    modes.sort()
    mode = modes[1]
else:
    mode = modes[0]
    
print(round(sum(nums) / len(nums))) 
print(nums[int(len(nums) / 2)])
print(mode)
print(nums[-1] - nums[0])