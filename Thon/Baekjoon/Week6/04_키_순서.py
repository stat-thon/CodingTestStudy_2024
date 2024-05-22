### 2458 - 키 순서
# 고민: 40분
# 코딩: 포기

# 플로이드-워셜 알고리즘
import sys

#입력
N, M = map(int, input().split())
height = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    tall, short = map(int, sys.stdin.readline().split())
    height[tall][short] = 1

#플로이드 와샬 알고리즘
for k in range(1, N+1): #경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(1, N+1):
        for j in range(1, N+1):
            if height[i][j] == 1 or (height[i][k] ==1 and height[k][j] == 1):
                height[i][j] = 1 #자신보다 작은 경우


#출력
answer = 0
for i in range(1, N+1):
    known_height = 0
    for j in range(1, N+1):
        known_height += height[i][j] + height[j][i] #자신보다 작은사람과 큰사람의 합
    if known_height == N-1: #자신의 키 순서를 알 경우
        answer += 1
print(answer)



### 풀이 2
from collections import defaultdict
import sys
input = sys.stdin.readline


def dfs(start, currNode, visited):
    visited[currNode] = True
    for nextNode in graph[currNode]:
        if not visited[nextNode]:
            height[start].add(nextNode)
            height[nextNode].add(start)
            dfs(start, nextNode,visited)


# 각 학생별로 자신보다 키가 큰 사람, 작은 사람을 저장하는 딕셔너리
height = defaultdict(set)
answer = 0
n, m = map(int, input().split())

# 키가 큰 사람에서 작은 방향으로 향하는 간선 그래프
graph = [[] for _ in range(n+1)] 
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 자신을 시작점으로 깊이 우선 탐색
# 시작점에서 출발하면서 거친 모든 노드는 시작점보다 키가 작다.
for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i, i, visited)

# 자신보다 키가 큰 사람 + 작은 사람의 정보가 N-1명이면 가능
for i in range(1, n+1):
    if len(height[i]) == n-1:
        answer += 1
print(answer)