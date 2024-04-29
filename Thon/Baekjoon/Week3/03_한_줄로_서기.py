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



### 비교답안
import sys

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
temp = [0] * n

# 반복문을 통해 각 자리에 들어갈 사람을 확인
for i in range(n):
    cnt = 0 # 자신의 왼쪽에 키 큰 사람의 수

    # 반복문을 통해 모든 사람을 확인
    for j in range(n):
        # 자신의 왼쪽에 키 큰 사람의 수가 맞고 그 자리에 아무도 없다면
        if cnt == m[i] and temp[j] == 0:
            temp[j] = i + 1
            break

        # 자리에 아무도 없다면 자신의 왼쪽에 키 큰 사람의 수를 카운트
        elif temp[j] == 0:
            cnt += 1

print(*temp)