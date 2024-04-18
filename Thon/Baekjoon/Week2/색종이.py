### 색종이
# 고민: 30분
# 코딩: 5분

n = int(input())

coord = [[0 for _ in range(100)] for _ in range(100)]

# 인덱스 - 1

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            coord[i - 1][j - 1] = 1
            
cnt = 0
for i in range(100):
    for j in range(100):
        if coord[i][j] == 1:
            cnt += 1
            
print(cnt)