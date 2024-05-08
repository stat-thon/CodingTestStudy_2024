### 영역 구하기
# 고민: 15분
# 코딩: 20분

import sys
M, N, K = map(int, sys.stdin.readline().split())

area = [[0] * N for _ in range(M)]

for _ in range(K):
    lx, ly, rx, ry = map(int, sys.stdin.readline().split())

    for i in range(lx, rx):
        for j in range(ly, ry):
            area[j][i] = 1

# recursion error 떠서 bfs로..

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global cnt

    dq = deque()
    dq.append((x, y))
    
    while dq:

        qx, qy = dq.popleft()
        
        for d in range(4):
            nx = qx + dx[d]
            ny = qy + dy[d]

            if 0 <= ny < N and 0 <= nx < M:
                if visited[nx][ny] == 0 and area[nx][ny] == 0:
                    cnt += 1
                    visited[nx][ny] = 1
                    dq.append((nx, ny))
                

result = []
visited = [[0] * N for _ in range(M)]

for i in range(M):
    for j in range(N):
        if area[i][j] == 0 and visited[i][j] == 0:            
            visited[i][j] = 1
            cnt = 1
            bfs(i, j)
            result.append(cnt)

print(len(result))
print(*sorted(result))