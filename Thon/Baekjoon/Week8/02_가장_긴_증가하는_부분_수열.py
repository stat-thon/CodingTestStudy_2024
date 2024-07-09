### 11053 - 가장 긴 증가하는 부분 수열
# 고민: 10분
# 코딩: 답 봄

N = int(input())
arr = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))