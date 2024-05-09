### 촌수계산
# 고민: 10분
# 코딩: 30분

import sys
from collections import deque

n = int(sys.stdin.readline())
q1, q2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

nodes = {i:[] for i in range(1, n + 1)}

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    nodes[x].append(y)
    nodes[y].append(x)


visited = [0] * (n + 1)

def bfs(node, goal):

    dq = deque()
    dq.append((node, 0))
    visited[q1] = 1
    
    while dq:
        q, cnt = dq.popleft()

        if nodes[q]:
            for nq in nodes[q]:
                if nq == goal:
                    return cnt + 1
                
                if visited[nq] == 0:
                    visited[nq] = 1
                    dq.append((nq, cnt + 1))
    return -1

print(bfs(q1, q2))