N = int(input())

cards = list(range(1, N + 1))
endWith = 1

while len(cards) > 1:
    if endWith == 1:
        if len(cards) % 2 == 1:
            endWith = 0
        else:
            endWith = 1
        cards = cards[1::2]
    else:
        if len(cards) % 2 == 1:
            endWith = 1
        else:
            endWith = 0
        cards = cards[::2]
    
print(cards[0])

## deque를 이용하면 시간 초과하지 않고 해결할 수 있다
'''
from collections import deque

N = int(input())
deque = deque([i for i in range(1, N+1)])

while(len(deque) >1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)
    
print(deque[0])
'''
  
## 규칙을 찾아도 빠르게 풀 수 있다
# [ INPUT - 2**(INPUT>2의 제곱) ] * 2이다.