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
    
    
### 답안 참고
ans=[]
while True:
  s=input()
  if '-' in s:
    break
  stack=[]
  cnt=0
  for i in s:
    if not stack and i=='}':
      cnt+=1
      stack.append("{")
    elif stack and i=='}':
      stack.pop()
    else:
      stack.append(i)
  cnt+=len(stack)//2
  ans.append(cnt)
for i in range(len(ans)):
  print(f"{i+1}. {ans[i]}")