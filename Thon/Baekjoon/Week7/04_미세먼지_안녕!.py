### 17144 - 미세먼지 안녕!
# 고민: 10분
# 코딩: 1시간

### 공기청정 파트를 틀려서 이 부분만 답안 참고하고 수정

import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

room = []

for _ in range(R):
    room.append(list(map(int, input().split())))

for r in range(R):
    if room[r][0] == -1:
        air_u = r
        break

air_d = air_u + 1

# 참고 부분
def air_up():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = air_u, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == air_u and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        room[x][y], before = before, room[x][y]
        x = nx
        y = ny

# 참고 부분
def air_down():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = air_d, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == air_d and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        room[x][y], before = before, room[x][y]
        x = nx
        y = ny


## 아래는 직접
nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]

for _ in range(T):
    new_room = [[0] * C for _ in range(R)]

    # 1. 확산
    for r in range(R):
        for c in range(C):
            
            if room[r][c] >= 5: # 확산 가능한 좌표
                
                minus = 0 # 기존 방에 남은 양을 계산하기 위함
                for d in range(4): # 4방향
                    x = r + nx[d]
                    y = c + ny[d]
                    
                    dirt = int(room[r][c] / 5) # 확산량
                    
                    
                    if 0 <= x < R and 0 <= y < C and (x, y) not in ((air_d, 0), (air_u, 0)):
                        minus += dirt
                        new_room[x][y] += dirt # 확산

                # 기존 방에 남은 양 확산 후 남은 양 더함
                new_room[r][c] += (room[r][c] - minus)
            elif room[r][c] == -1:
                new_room[r][c] = room[r][c]
            else:
                new_room[r][c] += room[r][c]
    room = new_room
    
    # 2. 공기 청정
    air_up()
    air_down()

#
result = 2
for r in range(R):
    result += sum(room[r])

print(result)


### 큐로 구현 (근데 느림)
import sys
from collections import deque
# input = sys.stdin.readline

R, C, T = map(int, input().split())

room = []

for _ in range(R):
    room.append(deque(map(int, input().split())))

for r in range(R):
    if room[r][0] == -1:
        air_u = r
        break

air_d = air_u + 1

def air_circulator():
    
    ## upper
    # ↓
    for i in range(air_u - 1, 0, -1):
        room[i][0] = room[i - 1][0]

    # ←
    room[0].popleft()

    # ↑
    room[0].append(room[1][-1])
    
    for i in range(1, air_u):
        room[i][-1] = room[i + 1][-1]

    # →
    room[air_u].pop()
    room[air_u].insert(1, 0)

    ## lower
    # ↑
    for i in range(air_d + 1, R - 1):
        room[i][0] = room[i + 1][0]

    # ←
    room[R - 1].popleft()

    # ↓
    room[R - 1].append(room[R - 2][-1])
    
    for i in range(R - 2, air_d, -1):
        room[i][-1] = room[i - 1][-1]

    # →
    room[air_d].pop()
    room[air_d].insert(1, 0)
    

# 시뮬레이션
nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]

for _ in range(T):
    new_room = [deque([0] * C) for _ in range(R)]

    # 1. 확산
    for r in range(R):
        for c in range(C):
            
            if room[r][c] >= 5: # 확산 가능한 좌표
                
                minus = 0 # 기존 방에 남은 양을 계산하기 위함
                for d in range(4): # 4방향
                    x = r + nx[d]
                    y = c + ny[d]
                    
                    dirt = int(room[r][c] / 5) # 확산량
                    
                    if 0 <= x < R and 0 <= y < C and (x, y) not in ((air_d, 0), (air_u, 0)):
                        minus += dirt
                        new_room[x][y] += dirt # 확산

                # 기존 방에 남은 양 확산 후 남은 양 더함
                new_room[r][c] += (room[r][c] - minus)
            elif room[r][c] == -1:
                new_room[r][c] = room[r][c]
            else:
                new_room[r][c] += room[r][c]
    room = new_room
    
    # 2. 공기 청정
    air_circulator()
    

result = 2
for r in range(R):
    result += sum(room[r])

print(result)
