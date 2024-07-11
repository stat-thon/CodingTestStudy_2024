### 11052 - 카드 구매하기
# 고민: 60분
# 코딩: 20분

N = int(input())
prices = list(map(int, input().split()))

def solution():
    dp = [0] * N
    dp[0] = prices[0]

    if N == 1:
        return dp[0]
    
    dp[1] = max(dp[0] + prices[0], prices[1])
    
    if N == 2:
        return dp[1]
    
    for i in range(2, N):
        MAX = prices[i]
        for j in range(1, i):
            MAX = max(dp[i - j] + prices[j - 1], MAX)

        dp[i] = MAX
        
    return dp[-1]

print(solution())