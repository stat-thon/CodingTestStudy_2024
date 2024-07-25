### 2002 - 추월
# 고민: 10분
# 코딩: 30분

import sys
input = sys.stdin.readline

N = int(input())
entry = [input() for _ in range(N)]
out = [input() for _ in range(N)]

cnt = 0
for i in range(N):
    out_idx = out.index(entry[i])

    for car in entry[:i]:
        if car not in out[:out_idx]:
            cnt += 1
            break

print(cnt)

# 완전 탐색이라 오래 걸림