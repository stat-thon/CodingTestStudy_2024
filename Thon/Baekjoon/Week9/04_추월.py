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

### 답안 참고
import sys
input = sys.stdin.readline
N = int(input())
seq = {}
for i in range(N):
    s = input().strip()
    seq[s] = i

last = 0
visited = [0] * N
ans = 0
for _ in range(N):
    n = seq[input().strip()]
    visited[n] = 1
    if last < n: ans += 1
    elif last == n:
        while last < N and visited[last]:
            last += 1
print(ans)