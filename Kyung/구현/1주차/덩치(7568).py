# 전역탐색

## 처음에 정렬로 접근했으나 공동순위 계산에서 막힘
## 전역탐색으로 그냥 했는데, 더 효과적 방법 있는지는 모르게씀..

import sys
n = int(input())

size = []  # 몸무게, 키 담아두는 공간
for _ in range(n) :
    x, y = map(int, sys.stdin.readline().strip().split())
    size.append([x,y])

for i in size:   # i[0] : 몸무게 / i[1] : 키
    rank = 1
    for j in size:
        if i[0] < j[0] and i[1] < j[1]:   # 이렇게 하면 자동으로 공동순위까지 고려
                rank += 1
    print(rank, end = " ")