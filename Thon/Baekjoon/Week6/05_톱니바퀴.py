### 톱니바퀴 - 14891
# 고민: 20분
# 코딩: 40분 후 답안 봄

import sys
from collections import deque

# input = sys.stdin.readline

wheels = []
for _ in range(4):
    wheels.append(deque(list(input())))

K = int(input())
R = [list(map(int, input().split())) for _ in range(K)]

def left(num, direction):
    if num < 0:
        return
    
    if wheels[num][2] != wheels[num + 1][6]:
        left(num - 1, -direction)
        wheels[num].rotate(direction)

def right(num, direction):
    if num > 3:
        return

    if wheels[num][6] != wheels[num - 1][2]:
        right(num + 1, -direction)
        wheels[num].rotate(direction)

# 반복문 시행
for i in range(K):
    num = R[i][0] - 1
    direction = R[i][1]
    left(num - 1, -direction)
    right(num + 1, -direction)
    wheels[num].rotate(direction)

score = 0
for i, s in enumerate([1, 2, 4, 8]):
    if wheels[i][0] == '1':
        score += s

print(score)