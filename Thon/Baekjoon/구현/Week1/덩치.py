### 분수찾기
# 고민: 2분
# 코딩: 30분 -> 틀려서 답 봄


n = int(input())

result = []
data = []
for i in range(n):

    w, h = map(int, input().split())
    data.append((w, h))


for i in range(n):
    
    cnt = 1
    for j in range(n):

        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:

            cnt += 1

    
    result.append(cnt)


print(*result)