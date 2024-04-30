from collections import deque

T = int(input())   # 전체 테스트케이스 갯수
for _ in range(T) :
    n, m = map(int,input().split())  # n : 문서 갯수,  m : 관심문서 인덱스 위치
    
    imp = list(map(int,input().split()))
    imp = deque((idx, val) for idx, val in enumerate(imp))
    tmp = []
    
    while imp :
        if len(imp) == 1 :   # 1일 때 필터링 안해주면 밑의 imp[0][1] < imp[k][1] 부분에서 인덱스 에러뜸
            tmp.append(imp.popleft())
            print(len(tmp))
            break
        
        k = 1
        while k < len(imp) :   # for문의 index와 append(popleft())를 함께 적용하면 작동 오류 생김
            if imp[0][1] < imp[k][1] :   
                imp.append(imp.popleft())
                break
            k += 1

        else :
            tmp.append(imp.popleft())
            if tmp[-1][0] == m :
                print(len(tmp))
                break
