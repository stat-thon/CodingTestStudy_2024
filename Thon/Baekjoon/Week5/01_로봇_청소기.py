### 14503 - 로봇청소기
# 고민: 10분
# 코딩: 35분

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
area = []

for _ in range(N):
    area.append(list(map(int, sys.stdin.readline().split())))

forward_moving = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
back_moving = {0: [1, 0], 1: [0, -1], 2: [-1, 0], 3: [0, 1]}
turn_moving = {0: [3, 2, 1, 0],
              1: [0, 3, 2, 1],
              2: [1, 0, 3, 2],
              3: [2, 1, 0, 3]}


dq = deque()
dq.append((r, c, d))

mdx = [-1, 1, 0, 0]
mdy = [0, 0, -1, 1]

cleaned = 0
while dq:
    
    x, y, d = dq.popleft()
    
    # 1. 청소되지 않은 칸인경우
    if area[x][y] == 0:
        area[x][y] = 2
        cleaned += 1
        
    # 2. 주변 4칸이 청소되지 않은 칸이 없는 경우
    cnt = 0
    for i in range(4):
        nx = x + mdx[i]
        ny = y + mdy[i]
            
        if area[nx][ny] in (1, 2):
            cnt += 1
                
    # 2-1. 청소되지 않은 칸이 없음
    if cnt == 4:
        dx, dy = back_moving[d]
        
        nx = x + dx
        ny = y + dy
        
        if area[nx][ny] == 1:
            break
            
        else:
            dq.append((nx, ny, d))
            
    # 2-2. 청소되지 않은 칸이 하나라도 있음
    else:
        
        # 반시계 방향으로 90도 회전
        for i in turn_moving[d]:
            
            # 전진 방향
            dx, dy = forward_moving[i]
            
            nx = x + dx
            ny = y + dy
            
            # 청소되지 않은 칸으로 이동
            if area[nx][ny] == 0:
                dq.append((nx, ny, i))
                break # 이후 90도 회전은 queue에 추가 할 필요 X
                
                
print(cleaned)