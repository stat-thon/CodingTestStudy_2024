n = int(input())
board = list([0]*101 for _ in range(100))

for _ in range(n) :
    a, b = map(int, input().split())

    for i in range(a, a+10) :
        for j in range(b, b+10) :
            board[i][j] = 1

answer = 0
for k in range(100) :
    answer += board[k].count(1)  # count함수 기억하기

print(answer)