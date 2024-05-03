### RGB거리
# 고민: 15분
# 코딩: 15분 답 봄

import sys

N = int(sys.stdin.readline())

cost = []
for _ in range(N):
    
    cost.append(list(map(int, sys.stdin.readline().split())))
    
MIN = 1e9

def dp(i, level, total_cost):
    global MIN
    
    if total_cost >= MIN:
        return
    
    if level == N - 1:
        MIN = min(MIN, total_cost)
        return
    
    for color in range(3):
        if color != i:
            dp(color, level + 1, total_cost + cost[level + 1][color])

# print
for i in range(3):
    dp(i, 0, cost[0][i])
    
print(MIN)


### 답안 비교
n = int(input())
a = [0]*n

for i in range(n):
    a[i] = list(map(int,input().split()))
    
for i in range(1,n): # 1부터 시작하는 이유는 다음 입력값이 이전 입력값의 최소값을 사용하기때문이다
    a[i][0]= min(a[i-1][1],a[i-1][2]) + a[i][0]
    a[i][1]= min(a[i-1][0],a[i-1][2]) + a[i][1]
    a[i][2]= min(a[i-1][0],a[i-1][1]) + a[i][2]

print(min(a[n-1][0],a[n-1][1],a[n-1][2]))