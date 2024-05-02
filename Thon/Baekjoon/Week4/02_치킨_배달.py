### 치킨 배달
# 고민: 15분
# 코딩: 7분

import sys

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
            
from itertools import combinations

MIN = 1e9

for coords in combinations(chicken, M):
    
    total_dist = 0
    
    for h in house:
        house_min = 1e9
        
        for c in coords:
            house_min = min(house_min, abs(h[0] - c[0]) + abs(h[1] - c[1]))
            
        total_dist += house_min
        
    MIN = min(MIN, total_dist)
    
print(MIN)


### 답안 비교
ans = 1e9
def solve():
    global ans
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    houses = []
    chickens = []
    chicken_dists = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                houses.append((i, j))
            elif board[i][j] == 2:
                chickens.append((i, j))


    for r1, c1 in houses:
        chicken_dists.append([])
        for idx, (r2, c2) in enumerate(chickens):
            chicken_dists[-1].append((abs(r1 - r2) + abs(c1 - c2), idx))
        chicken_dists[-1].sort(key=lambda x:x[0])

    ans = 1e9
    visited = [False for _ in range(len(chickens))]
    def dfs(depth, start):
        global ans
        if depth == M:
            tmp = 0
            for D in chicken_dists:
                for distance, idx in D:
                    if visited[idx]:
                        tmp += distance
                        break
            ans = min(ans, tmp)
            return

        for i in range(start, len(chickens)):
            if not visited[i]:
                visited[i] = True
                dfs(depth + 1, i + 1)
                visited[i] = False

    dfs(0, 0)
    print(ans)

solve()