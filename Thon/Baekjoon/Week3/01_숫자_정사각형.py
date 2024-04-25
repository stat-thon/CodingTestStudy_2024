### 숫자 정사각형
# 고민: 7분
# 코딩: 13분

import sys

n, m = map(int, input().split())

full_length = min(n, m)

square = []
for _ in range(n):
    
    square.append(list(map(int, input())))
    
# 풀이
MAX = 1
if full_length == 1:
    pass
else:
    
    for l in range(2, full_length + 1):
        for i in range(0, n - l + 1):
            for j in range(0, m - l + 1):
            
                left_up = square[i][j]
                left_down = square[i + l - 1][j]
                right_up = square[i][j + l - 1]
                right_down = square[i + l - 1][j + l - 1]
            
                if left_up == left_down and left_up == right_up and left_up == right_down:
                    MAX = max(MAX, l)
                
print(MAX ** 2)