# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
result = []
words = [[] for i in range(50)]

N = int(input())
for i in range(N):
    word = input()
    words[len(word) - 1].append(word)

for i in range(len(words)):
    if len(words[i]) != 0:    
        words[i] = list(set(words[i]))
        words[i].sort()
        result += words[i]

for i in range(len(result)):
    print(result[i])
    

# 14분 56초 소요