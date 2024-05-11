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
