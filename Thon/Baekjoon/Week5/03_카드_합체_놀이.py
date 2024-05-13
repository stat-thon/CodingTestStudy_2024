### 15903 - 카드 합체 놀이
# 고민: 5분
# 코딩: 5분

import heapq

n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

for _ in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)

    z = x + y

    heapq.heappush(cards, z)
    heapq.heappush(cards, z)

print(sum(cards))
