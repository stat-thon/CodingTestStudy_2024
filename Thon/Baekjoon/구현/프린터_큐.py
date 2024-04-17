### 프린터 큐
# 구현: 5분
# 코딩: 20분

from collections import deque

def printer(dq):
    
    cnt = 0
    if len(dq) == 1:
        return 1
    
    while dq:
        
        q = dq.popleft()
        im = importance.popleft()
        
        # 중요도가 더 높은 것이 남아 있다면
        if dq and max(importance) > im:
            dq.append(q)
            importance.append(im)
            
        else:
            cnt += 1
            
            if q == 1:
                return cnt
            
r = int(input())

for _ in range(r):
    n, m = map(int, input().split())
    importance = deque(map(int, input().split()))
    
    dq = deque([0 for _ in range(n)])
    dq[m] = 1
    
    print(printer(dq))



# 시행착오 공유 1. dq가 중간에 빈 경우를 고려하지 않음
def printer(dq):
    
    cnt = 0
    if len(dq) == 1:
        return 1
    
    while dq:
        
        q = dq.popleft()
        im = importance.popleft()
        
        # dq가 중간에 빈 경우를 고려하지 않음
        if max(importance) > im:
            dq.append(q)
            importance.append(im)
            
        else:
            cnt += 1
            
            if q == 1:
                return cnt
            


# 시행착오 공유 2. and 조건의 앞에서 dq를 검사하지 않고 뒤로 넣었더니 max()가 계산 안돼서 오류 발생
def printer(dq):
    
    cnt = 0
    if len(dq) == 1:
        return 1
    
    while dq:
        
        q = dq.popleft()
        im = importance.popleft()
        
        # dq가 비는 조건을 and 뒤로 넣었더니 max함수 계산 못해서 오류 발생
        if max(importance) > im and dq:
            dq.append(q)
            importance.append(im)
            
        else:
            cnt += 1
            
            if q == 1:
                return cnt