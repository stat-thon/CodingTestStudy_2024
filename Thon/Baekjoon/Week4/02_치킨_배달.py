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