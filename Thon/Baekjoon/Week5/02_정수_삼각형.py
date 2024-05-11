### 1932 정수 삼각형
# 고민: 20분
# 코딩: 15분

import sys
n = int(sys.stdin.readline())

result = [int(sys.stdin.readline())]

if n == 1:
    print(result[0])
    
else:
    for _ in range(n - 1):
        
        nums = list(map(int, sys.stdin.readline().split()))
        
        length = len(nums)
        cnt = []
        for i in range(length):
            
            if i == 0:
                cnt.append(result[0] + nums[0])
                
            elif i == length - 1:
                cnt.append(nums[i] + result[i - 1])
                
            else:
                cnt.append(max(nums[i] + result[i - 1], nums[i] + result[i]))
        
        result = cnt
                
    print(max(result))



### 비교 답안
# 1932  정수 삼각형 (파이썬 Python)
n = int(input())
dp = []

for i in range(n) :                            ## 입력값 이차원리스트 형태로 dp테이블에 저장하기
    dp.append(list(map(int,input().split())))

print(dp)
print(dp[1][0])

for i in range(1,n) :                           ## 행을 기준으로 for문 구성
    for j in range(0,i+1) :                     ## 열을 기준으로 for문 구성
        if j == 0 :
            dp[i][0] += dp[i-1][0]              # 0열끼리 더하기
        elif j == i :
            dp[i][j] += dp[i-1][j-1]            # 마지막 열끼리 더하기
        else :
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])    # 두 화살표중 더 큰 경우 받아들이기

print(max(dp[n-1])) 

# 출처: https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-1932-%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%95-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python