### 2841 - 외계인의 기타 연주
# 고민: 12분
# 코딩: 5분

import sys
N, P = map(int, sys.stdin.readline().split())

move = 0
stack = [[0] for _ in range(6)]

for _ in range(N):
    line, plat = map(int, sys.stdin.readline().split())

    if stack[line - 1][-1] < plat:
        stack[line - 1].append(plat)
        move += 1

    elif stack[line - 1][-1] > plat:

        while stack[line - 1][-1] > plat:
            stack[line - 1].pop()
            move += 1

        if stack[line - 1][-1] == plat:
            pass
        else:
            stack[line - 1].append(plat)
            move += 1
    else:
        pass

print(move)


### 답안 비교 + 최적화
import sys
N, P = map(int, sys.stdin.readline().split())

move = 0
stack = [[0] for _ in range(6)]

for _ in range(N):
    line, plat = map(int, sys.stdin.readline().split())

    while stack[line - 1][-1] > plat:
        stack[line - 1].pop()
        move += 1

    if stack[line - 1][-1] == plat:
        continue
    
    stack[line - 1].append(plat)
    move += 1

print(move)