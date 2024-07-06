### 1389 - 케빈 베이컨의 6단계 법칙
# 고민: 5분
# 코딩: 40분

import sys
from collections import deque
# input = sys.stdin.readline

N, M = map(int, input().split())
rel = [deque([0] * N) for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    rel[a - 1][b - 1] = 1
    rel[b - 1][a - 1] = 1

result = [[0] * N for _ in range(N)]

for i in range(N):
    
    visited = [0] * N
    visited[i] = 1

    dq = deque()
    dq.append((i, 0))

    while dq:
        q, dist = dq.popleft()
        
        for j in range(N):

            if visited[j] == 0 and rel[q][j] == 1 and result[i][j] == 0:
                visited[j] = 1
                result[i][j] = dist + 1
                dq.append((j, dist + 1))

MIN = 1e9
user = -1
for i, cnt in enumerate(list(map(sum, result))):
    if MIN > cnt:
        user = i + 1
        MIN = cnt
print(user)


### 시간 복잡도 감소
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
rel = [deque() for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    rel[a - 1].append(b - 1)
    rel[b - 1].append(a - 1)

result = [0] * N


def bfs(i):    
    visited = [0] * N
    visited[i] = 1

    dq = deque()
    dq.append((i, 0))

    while dq:
        q, dist = dq.popleft()
        
        for node in rel[q]:

            if visited[node] == 0:
                visited[node] = 1
                result[i] += dist + 1
                dq.append((node, dist + 1))

for i in range(N):
    bfs(i)
print(result.index(min(result)) + 1)