### 프렌즈4블록
# 구현
# 고민: 40분
# 코딩: 25분

def solution(m, n, board):
    
    board = [list(b) for b in board]
    
    iter = m*n//4
    
    while iter:
        
        delete_set = [set() for _ in range(n)]
    
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    delete_set[j].add(i)
                    delete_set[j].add(i+1)
                    delete_set[j+1].add(i)
                    delete_set[j+1].add(i+1)
        
    
        # 삭제 우선 반영
        for c in range(n):
            for r in delete_set[c]:
                board[r][c] = '0'
            
        # 한 칸씩 끌어오기
        for c in range(n):
            col_list = [board[i][c] for i in range(m)]
            col_str = "".join(col_list).replace('0', "").zfill(m)
        
            for i, s in enumerate(col_str):
                board[i][c] = s
                
        iter -= 1
    
    print(board)
    
    cnt = 0
    for i in range(m):
        for j in range(n):
            if board[i][j] == '0':
                cnt += 1
    
    return cnt