### 2636 - 치즈
# 고민: 25분
# 코딩: 20분

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(H)]

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 반복실행
t = 0
while sum(map(sum, cheese)) != 0:
    cnt = sum(map(sum, cheese))
        
    # 초기화
    dq = deque()
    dq.append((0, 0))

    visited = [[0] * W for _ in range(H)]
    visited[0][0] = 1
    
    # bfs
    while dq:
        x, y = dq.popleft()
        
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
        
            if 0 <= nx < H and 0 <= ny < W and visited[nx][ny] == 0:
            
                if cheese[nx][ny] == 0: # 공기가 퍼지는 경로만 보려고
                    visited[nx][ny] = 1
                    dq.append((nx, ny))
            
                elif cheese[nx][ny] == 1: # 경계
                    visited[nx][ny] = -1 # 경계는 visited에 -1로 표시하고 그 좌표로 안 움직임
                    continue
    
    # 경계 지우기
    for i in range(H):
        for j in range(W):
            if visited[i][j] == -1:
                cheese[i][j] = 0
    t += 1
    
print(t)
print(cnt)


### 참고 답안
n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for i in range(n)]
visit = [list(0 for i in range(m)) for i in range(n)]
melt = [(0,0)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(melt, time):
    count = len(melt)
    find = []
    while melt:
        x, y = melt.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (nx >= 0 and nx < n) and (ny >= 0 and ny < m):
                if visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    if cheese[nx][ny] == 0:
                        melt.append((nx, ny))
                    elif cheese[nx][ny] == 1:
                        find.append((nx, ny))
    if find:
        return bfs(find, time + 1)
    else:
        return time, count
time, count = bfs(melt, 0)
print(time)
print(count)