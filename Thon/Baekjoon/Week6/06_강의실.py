### 1376 - 강의실
# 고민: 30분
# 코딩: 1시간 

## 시간초과
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
lec_list = []
for _ in range(n):
    num, s, e = map(int, input().split())
    lec_list.append([s, e])
    
lec_list = sorted(lec_list)

hq = [[]]
dq = deque(lec_list)
hq[0].append(dq.popleft())

while dq:
    q = dq.popleft()
    did_it = 0
    
    for nq in hq:
        if nq[-1][1] <= q[0]:
            nq.append(q)
            did_it = 1
            break
    
    if did_it == 0:
        hq.append([q])

print(len(hq))


### 풀이
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    _, s, e = map(int, input().split())
    arr.append((s, e))

from heapq import heappop, heappush
h = []
for (s, e) in sorted(arr, key=lambda x: x[0]):
    if h and h[0] <= s:
        heappop(h)
    heappush(h, e)
print(len(h))