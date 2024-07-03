### 14501 - 퇴사
# 고민: 30분
# 코딩: 15분

import sys
#input = sys.stdin.readline

N = int(input())
consult = []

for _ in range(N):
    consult.append(tuple(map(int, input().split())))

MAX = 0
def dfs(n, rev):

    global MAX

    if n == N:
        MAX = max(MAX, rev)
        return

    if n + consult[n][0] <= N: # 상담시 초과 하지 않으면
        dfs(n + consult[n][0], rev + consult[n][1])
        
    dfs(n + 1, rev)
    return

dfs(0, 0)
print(MAX)


### 답안 비교
# input
n = int(input())
l = []
for i in range(n):
  l.append(list(map(int, input().split())))

# 수익 기록
an = [0] * (n + 1)

# 퇴사 전날부터 거꾸로
for i in range(n - 1, -1, -1):
  
  if i + l[i][0] > n: # 상담 시 초과 하면
      
    an[i] = an[i + 1] # 상담이 안 되므로 다음날의 수익을 기록
    
  else: # 상담 시 초과 X
    
    # 해당 상담 수익 + 상담으로 지난 날 / 다음날 수익 중  MAX 기록
    an[i] = max(l[i][1] + an[i + l[i][0]], an[i + 1])

print(an[0])