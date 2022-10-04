global numbers

n = int(input())
numbers = list(map(int, input().split()))
cnt = 0

# dp로 뒤에서부터 내려감
'''
number[-1] 을 만들 수 있는 수
-2 를 보고 거기에 뭘 더해야 혹은 빼야 -1을 만들 수 있는지 확인 
그게 20을 넘으면 탈락 혹은 음수 뭐시기

ex) 8 3 2 4 8 7 2 4 0 8 8
8 - 8 + 0 아니면 16 - 8

0 아니면 16이어야 함
+ - 0 아니면 + 16

 +, -
 

'''



