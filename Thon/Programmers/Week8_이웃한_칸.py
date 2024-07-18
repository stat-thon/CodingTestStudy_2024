### [PCCE 기출문제] 9번 / 이웃한 칸
# 고민: 3분
# 코딩: 3분

def solution(board, x, y):
    
    cnt = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        
        if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
            if board[x][y] == board[nx][ny]:
                cnt += 1
            
    return cnt