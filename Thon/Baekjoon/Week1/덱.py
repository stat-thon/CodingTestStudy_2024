### 스택
# 고민: 3분
# 코딩: 23분


from collections import deque
import sys

dq = deque()

n = int(input())

for _ in range(n):
    
    m = sys.stdin.readline().split()
    
    if len(m) == 2:
        order, number = m
        number = int(number)
        
    else:
        order = m[0]
    
        
    
    if order == "push_front":
        
        dq.appendleft(number)
        
    elif order == "push_back":
        
        dq.append(number)
        
    elif order == "pop_front":
        
        if dq:
            q = dq.popleft()
            print(q)
            
        else:
            print(-1)
        
        
    elif order == "pop_back":
        
        if dq: 
            q = dq.pop()
            print(q)
           
        else:
            print(-1)
            
    elif order == "size":
        
        print(len(dq))
        
    elif order == "empty":
        
        if dq:
            print(0)
        else:
            print(1)
            
    elif order == "front":
        
        if dq:
            print(dq[0])
            
        else:
            print(-1)
            
    elif order == "back":
        
        if dq:
            print(dq[-1])
            
        else:
            print(-1)
            
        
    
    

