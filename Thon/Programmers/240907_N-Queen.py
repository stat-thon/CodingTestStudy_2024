### N-Queen
# 알고리즘 : DFS, 백트래킹
# 고민: 30분
# 코딩: 30분
# 정답 봄

def solution(n):

	# 저장된 queen 위치 ls, 새로 두려는 위치 new
    def check(ls, new):
        for i in range(len(ls)):
        	# 같은 열에 퀸을 둔 적이 있거나, 대각 위치에 둔 적이 있다면, return False
            if new == ls[i] or (len(ls)-i) == abs(ls[i]-new):
                return False
        return True
        
    def dfs(n, ls):
    
       	# 정답 조건도 이렇게 두어서 굳이 cnt를 업데이트 하는 식으로 하지 않음
        if len(ls) == n:
            return 1
            
        # 끝 행이 아니라면, 다음 줄을 다시 탐색
        cnt = 0
        for i in range(n):
            
            # 대각선 위치, 기존에 둔 것과 겹치지 않는 위치
            if check(ls, i):
                cnt += dfs(n, ls + [i]) # 1차원 배열에 다른 퀸 위치를 append, 결과는 1 더하는 것으로 cnt 업데이트
                
        # 탐색 결과를 return
        return cnt
        
    return dfs(n, [])