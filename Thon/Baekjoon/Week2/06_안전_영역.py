### 안전 영역
# 고민: 5분
# 코딩: 30분 (초과)

import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())

area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, height):
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and area[nx][ny] > height:
            
            visited[nx][ny] = 1 # visit
            dfs(nx, ny, height)



MAX = 1

for height in range(max(map(max, area))):

    visited = [[0] * n for _ in range(n)]
    cnt = 0
    

    for i in range(n):
        for j in range(n):
            if area[i][j] > height and visited[i][j] == 0 :
                cnt += 1
                visited[i][j] = 1
                dfs(i, j, height)
    MAX = max(MAX, cnt)
print(MAX)