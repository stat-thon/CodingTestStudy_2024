### 4990 - 안정적인 문자열
# 고민: 20분
# 코딩: 10분

from collections import deque

def stable(s):

    dq = deque(s)
    stack = deque()

    while dq:
        q = dq.popleft()

        if q == '}' and stack and stack[-1] == '{':
            stack.pop()
            
        else:
            stack.append(q)
    
    cnt = 0
    if not stack:
        return cnt
        
    while stack:
        q1 = stack.popleft()
        q2 = stack.popleft()

        if q1 + q2 == '}{':
            cnt += 2
        else:
            cnt += 1
    
    return cnt

#import sys
#input = sys.stdin.readline

num = 1
while True:
    s = input()

    if '-' in s:
        break

    print(f'{num}. {stable(s)}')

    num += 1