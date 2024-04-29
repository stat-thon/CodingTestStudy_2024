### 한 줄로 서기
# 고민: 14분
# 코딩: 2분

n = int(input())
order = list(map(int, input().split()))
index = [i for i in range(n)]
result = [0] * n

for i, n in enumerate(order):
    
    new = index[n]
    result[new] += (i + 1)
    index.remove(new)

print(*result)