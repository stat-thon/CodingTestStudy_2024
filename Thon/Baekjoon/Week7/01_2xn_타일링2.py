### 11727 - 2xn 타일링 2
# 고민: 30분
# 코딩: 5분

n = int(input())
num = [1, 3]

def solution(n):
    
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        while len(num) != n:
            num.append(num[-1] + num[-2] * 2)
    return num[-1] % 10007

print(solution(n))


### 답안 비교
n = int(input())
dp=[0, 1, 3]

for i in range(3,n + 1):
    
    dp.append(dp[i - 1] + dp[i - 2] * 2)
    
print(dp[n] % 10007)