from collections import deque
n, m = map(int, input().split())

a = list(range(1,n+1))
a = deque(a)

answer = []
while a :
    for _ in range(m-1) :
        a.append(a.popleft())
    answer.append(a.popleft())

# 리스트 자체를 문자로 바꿀 수 있음
# 리스트 자체를 출력시 '['와 ']'를 replace 함수로 대체가능
print(str(answer).replace('[', '<').replace(']', '>'))


