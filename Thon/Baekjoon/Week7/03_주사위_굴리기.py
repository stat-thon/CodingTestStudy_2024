### 14499 - 주사위 굴리기
# 고민: 45분
# 코딩: 1시간

### 하..
import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
dice_map = []

for _ in range(N):
    dice_map.append(list(map(int, input().split())))

moves = list(map(int, input().split()))

dice = [0] * 6

def move_dice(d):
    if d == 1:
        dice_copy = [dice[0], dice[5], dice[1], dice[2], dice[4], dice[3]]
    elif d == 2:
        dice_copy = [dice[0], dice[2], dice[3], dice[5], dice[4], dice[1]]
    elif d == 3:
        dice_copy = [dice[2], dice[1], dice[4], dice[3], dice[5], dice[0]]
    else:
        dice_copy = [dice[5], dice[1], dice[0], dice[3], dice[2], dice[4]]

    return dice_copy


dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def move(d):

    global x, y, dice
    
    nx = x + dx[d - 1]
    ny = y + dy[d - 1]

    if 0 <= nx < N and 0 <= ny < M:
        x, y = nx, ny
        
        dice = move_dice(d)

        if dice_map[x][y] != 0: # 지도면이 0이 아님
            dice[5] = dice_map[x][y] # 주사위를 업데이트
            dice_map[x][y] = 0
        else: # 지도면이 0이면
            dice_map[x][y] = dice[5]
        
        return dice[2]

    else: # 지도 위치를 벗어나면
        return 'no'
    
for d in moves:
    result = move(d)
    if result != 'no':
        print(result)