# 입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 1 이상 99999 이하의 정수가 주어진다. 입력의 마지막 줄에는 0이 주어지며, 이 줄은 문제에 포함되지 않는다.

# 각 줄마다 주어진 수가 팰린드롬수면 'yes', 아니면 'no'를 출력한다.

candidate = ""
while True:
    yesno = "yes"
    candidate = input()
    if candidate == "0":
        break
    if len(candidate) % 2 == 1: 
        half = int((len(candidate) - 1) / 2)
    else:
        half = int(len(candidate) / 2 )
        
    for i in range(half):
        if candidate[i] != candidate[-(i + 1)]:
            yesno = "no"
            break
    print(yesno)
    
    # 18분 50초 소요
    