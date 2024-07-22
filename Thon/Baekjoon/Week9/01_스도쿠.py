### 2239 - 스도쿠
# 고민: 30분
# 코딩: 30분 못 풀고 답 봄

# 내 답안
import sys
# input = sys.stdin.readline
board = [list(map(int, input())) for _ in range(9)]
num_set = {i for i in range(1, 10)}

def garo(ind):
    a = set()
    for i in board[ind]:
        if i != 0:
            a.add(i)
    return num_set - a

def sero(ind):
    a = set()
    
    for i in range(9):
        if board[i][ind] != 0:
            a.add(board[i][ind])
    return num_set - a

def block(i, j):
    a = set()

    row, col = i // 3, j // 3
    for r in range(row * 3, row * 3 + 3):
        for c in range(col * 3, col * 3 + 3):
            if board[r][c] != 0:
                a.add(board[r][c])
    return num_set - a

def check(n):
    cnt = 0
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                g, s, b = garo(i), sero(j), block(i, j)
                cand = g & s & b
                if len(cand) == n:
                    board[i][j] = list(cand)[0]
                else:
                    cnt += 1
            else:
                cnt += 1
    return cnt

while sum(map(sum, board)) != 405:
    
    for i in range(1, 10):
        if check(i) != 81 and sum(map(sum, board)) != 405:
            break # 반복문 중단

for i in range(9):
    print(*board[i], sep = "")
    
# 예시는 풀리지만, 시간초과 발생 -> 반례를 보니, backtracking을 꼭 해야하는데 되돌릴 가능성 없이 답을 바로 넣은 게 문제 원인

# 답안 참고
# https://otugi.tistory.com/386
# 코딩이 깔끔한데, 애초에 이 문제 시간이 꽤 많이 걸리는 문제였음. 역시 개발자처럼은 못 풀겠음

def cal(x,y):
    return (x//3)*3 + (y//3)

def sol(n):
    if n == 81:
        for a in A:
            print(''.join(list(map(str, a))))
        return True
    x = n // 9
    y = n % 9
    if A[x][y]:
        return sol(n+1)
    else:
        for i in range(1,10):
            if not c1[x][i] and not c2[y][i] and not c3[cal(x,y)][i]:
                c1[x][i] = c2[y][i] = c3[cal(x,y)][i] = True
                A[x][y] = i
                if sol(n+1):
                    return True
                c1[x][i] = c2[y][i] = c3[cal(x,y)][i] = False
                A[x][y] = 0
    
    return False

A = [list(map(int, input())) for _ in range(9)]
c1 = [[False]*10 for _ in range(9)] # row
c2 = [[False]*10 for _ in range(9)] # col
c3 = [[False]*10 for _ in range(9)] # 3x3 square
for i in range(9):
    for j in range(9):
        if A[i][j]:
            c1[i][A[i][j]] = True   # i행에 A[i][j] 숫자가 사용됨
            c2[j][A[i][j]] = True   # j열에 A[i][j] 숫자가 사용됨
            c3[cal(i,j)][A[i][j]] = True # cal(i,j)번째 square에 A[i][j] 숫자가 사용됨
sol(0)