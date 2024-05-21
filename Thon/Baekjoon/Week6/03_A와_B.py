### 12904 - A와 B
# 고민: 20분
# 코딩: 포기

S = list(input())
T = list(input())

while len(T) != len(S):
    q = T.pop()
    if q == 'B':
        T = T[::-1]

if T == S:
    print(1)
else:
    print(0)