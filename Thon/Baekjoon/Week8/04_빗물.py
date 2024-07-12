### 14719 - 빗물
# 고민: 28분
# 코딩: 12분

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

g = blocks.index(max(blocks))

l, r = 0, w - 1
result = 0

while l < g - 1:
    cnt = 0
    for i in range(l + 1, g):
        if blocks[l] > blocks[i]:
            cnt += blocks[l] - blocks[i]
        else:
            break
    l = i
    result += cnt
    
while g + 1 < r:
    cnt = 0
    for i in range(r - 1, g, -1):
        if blocks[r] > blocks[i]:
            cnt += blocks[r] - blocks[i]
        else:
            break
    r = i
    result += cnt

print(result)


### 답안 참고
import sys
ans = 0

H, W = list(map(int, sys.stdin.readline().split()))
blocks = list(map(int, sys.stdin.readline().split()))

ans = 0

for i in range(1, W-1):
    l_max = max(blocks[:i])
    r_max = max(blocks[i+1:])
    
    cmp = min(l_max, r_max)
    
    if blocks[i] < cmp:
        ans += cmp - blocks[i]

print(ans)