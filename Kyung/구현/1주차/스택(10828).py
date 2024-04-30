import sys

n = int(input())   # 명령 개수
stack = []  # 명령에 따른 처리 대상 리스트

for _ in range(n) :
    # input으로 받으면 시간초과 뜸 strip()뒤에 붙여줘서 개행문자 제거하는 것 주의
    a = sys.stdin.readline().strip()    
    if 'push' in a :
        x, num = a.split()
        stack.append(int(num))
    else :
        if a == 'top' :
            if len(stack) == 0 :
                print(-1)
            else :
                print(stack[-1])
        elif a == 'size' :
            print(len(stack))
        elif a == 'empty' :
            if len(stack) == 0 :
                print(1)
            else :
                print(0)
        elif a == 'pop' :
            if len(stack) == 0 :
                print(-1)
            else :
                print(stack.pop())
    
        

