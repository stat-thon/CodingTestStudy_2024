# 규칙 찾는 것이 중요
## 규칙 못 찾아서 답안 봄

'''
1/1
1/2, 2/1
3/1, 2/2, 1/3
1/4, 2/3, 3/2, 4/1
5/1, 4/2, 3/3, 2/4, 1/5
'''
# 홀수 줄의 분자는 해당 line 숫자에서 -1씩 1까지 줄어듦
#           분모는 1에서 +1씩 해당 line 숫자까지 증가함
# 짝수 줄의 분자는 1에서 +1씩 해당 line 숫자까지 증가함
#           분모는 해당 line 숫자에서 -1씩 1까지 줄어듦

num = int(input())
line = 1 # line 초기값 설정

# num이 몇번째 줄에 있는지 확인
while num > line:
    num -= line
    line += 1
    
# 위 코드에서 나온 line은 몇 번째 줄에 있는지, num은 해당 line에서 몇 번째 값인지 의미
    
# 짝수 줄에 있는 경우
if line % 2 == 0:
    a = num
    b = line - num + 1
    
# 홀수 줄에 있는 경우
elif line % 2 == 1:
    a = line - num + 1
    b = num

print('{}/{}'.format(a,b))