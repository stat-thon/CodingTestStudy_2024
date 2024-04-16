
n = int(input())  # 그룹 단어인지 확인할 단어 개수
cnt = 0

for _ in range(n) :
    w = input()  # 단어 받기
    i = 0        # 현 단어의 각 철자에 대한 인덱스 초기값 설정
    while i < len(w) :    # 현 단어의 각 철자에 대해 순차적으로 반복문 돌기 
        if w[i] in w[:i] :     # 현재의 철자가 과거에 등장한 적이 있다면 
            if w[i] != w[i-1] :   # 그리고 현재의 철자가 바로 이전과 다르다면
                break    # 그룹단어가 아니므로 break
        i += 1
    else :     # 위의 while문 무사히 다 돌았다면 
        cnt += 1   # 카운트해주기
print(cnt)
