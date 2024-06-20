### 2458 - 키 순서
# 고민: 40분
# 코딩: 포기

# 풀이 1 - PyPy 컴파일러
# 플로이드-워셜 알고리즘
import sys
input = sys.stdin.readline
'''
플로이드-워셜 알고리즘은 임의의 노드 s에서 e까지 가는 데 걸리는 최단거리를 구하기 위해,
s와 e 사이의 노드인 m에 대해 s에서 m까지 가는 데 걸리는 최단거리와 m에서 e까지 가는 데 걸리는 최단거리를 이용한다.
시간복잡도는 O(V^3)
'''

# N : 학생들의 수(=노드 갯수), M : 비교 횟수(=간선 갯수)
N, M = map(int, input().split())

# 1. 그래프 초기화
MAX = 1e9
graph = [[MAX for _ in range(N + 1)] for _ in range(N + 1)]

# 2. 입력
for i in range(M):
    a, b = map(int, input().split())   # a < b
    graph[a][b] = 1

# 3. 플로이드 워셜 진행
for m in range(1, N + 1):  # 중간 지점
    for s in range(1, N + 1):   # 시작
        for e in range(1, N + 1):   # 끝
            # 시작 ~ 마지막 > 시작 ~ 가운데 + 가운데 + 끝 -> 갱신
            if graph[s][e] > graph[s][m] + graph[m][e]:
                graph[s][e] = graph[s][m] + graph[m][e]


# 4. 모든 학생과의 비교가 가능한 경우
#      == 거리가 INF가 아닌 학생의 수가 N-1인 경우
answer = 0
for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N+1):
        if graph[i][j] != MAX or graph[j][i] != MAX:
            cnt += 1

    if cnt == N-1:
        answer += 1

print(answer)





### 풀이 2 - Python3 컴파일러인데 시간도 빠름
import sys
input = sys.stdin.readline

def dfs(now, visit, graph):
    visit[now] = 1
    for nxt in graph[now]:
        if visit[nxt]:
            continue
        dfs(nxt, visit, graph)

def solution():
    
    # input 받고
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
    
    # visited 만들고
    visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    
    # dfs 돌리기
    for i in range(1, N + 1):
        dfs(i, visited[i], graph)

    result = 0
    for i in range(1, N + 1):
        cnt = 0
        for j in range(1, N + 1):
            if visited[i][j] or visited[j][i]:
               cnt += 1
        if cnt == N:
            result += 1

    print(result)

solution()