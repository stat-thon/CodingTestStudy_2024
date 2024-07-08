### 경로 찾기
# 고민: 10분
# 코딩: 20분

import sys
input = sys.stdin.readline

N = int(input()) # node 수

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

result = [[0] * N for _ in range(N)]

def dfs(i, n):
    
    for now in range(N):

        if visited[now] == 0 and graph[n][now] == 1:
            result[i][now] = 1
            visited[now] = 1
            dfs(i, now)

    return

for i in range(N):
    visited = [0] * N
    dfs(i, i)
    
for i in range(N):
    print(*result[i])
    
    
# 좀 더 줄임
import sys
input = sys.stdin.readline

N = int(input()) # node 수

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

def dfs(n):
    
    for now in range(N):
        if visited[now] == 0 and graph[n][now] == 1:
            visited[now] = 1
            dfs(now)
    return

for i in range(N):
    visited = [0] * N
    dfs(i)
    print(*visited)