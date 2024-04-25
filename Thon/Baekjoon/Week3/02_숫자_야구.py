### 숫자 야구
# 고민: 20분
# 코딩: 20분
## 시간 초과하여 답안 확인

import sys
from itertools import permutations

N = int(sys.stdin.readline().rstrip())

numbers = list(permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3))

for _ in range(N):
    question_number, strike, ball = map(int, sys.stdin.readline().split())
    question_number = list(str(question_number))
    removed = 0
	
    # 고친 부분
    for i in range(len(numbers)):
        strike_cnt = 0
        ball_cnt = 0
        
        # 요소가 제거된 만큼 인덱스 조절
        i -= removed
        
		# 스트라이크, 볼 개수 확인
        for j in range(3):
            if question_number[j] == numbers[i][j]:
                strike_cnt += 1
            elif question_number[j] in numbers[i]:
                ball_cnt += 1
        
        # 스트라이크 or 볼의 개수가 맞지 않으면 리스트에서 제거
        if strike_cnt != strike or ball_cnt != ball:
            numbers.remove(numbers[i])
            removed += 1

print(len(numbers))



### 답안 딕셔너리형 활용
import sys
from itertools import permutations

N = int(input())

numbers = dict()
for p in permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3):
    numbers[p] = 1



for _ in range(N):
    question_number, strike, ball = map(int, sys.stdin.readline().split())
    question_number = str(question_number)

    for k in numbers.keys():
    
        strike_cnt = 0
        ball_cnt = 0
    
        if numbers[k] != 0:
            for j in range(3):
                if question_number[j] == k[j]:
                    strike_cnt += 1
                elif question_number[j] in k:
                    ball_cnt += 1
                
        if strike_cnt != strike or ball_cnt != ball:
            numbers[k] = 0
    
cnt = 0

for v in numbers.values():
    if v == 1:
        cnt += 1
        
print(cnt)
