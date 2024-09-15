### 괄호 변환
# 스택, 큐, dfs
# 고민: 30분
# 코딩: 40분

def solution(p):
    
    from collections import deque
    dq = deque(p)
    
    def dfs(dq, result = ''):
        l, r = 0, 0
        tmp = ''
        stack = []
        
        # 1. 빈 문자열 반환
        if not dq:
            return result
        
        # 2. u, v분리
        while l != r or not tmp:
            
            q = dq.popleft()
            
            if q == '(':
                l += 1
                stack.append(q)
            else:
                r += 1
                
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(q)
            
            tmp += q
        
        # 4. 올바르지 않은 경우
        if stack: # 올바르지 않은 괄호 문자열
            
            # 4-1, 4-2, 4-3
            new = '(' + dfs(deque(dq), '') + ')' # dfs로 남은 dq에 대해서 하고
            
            # 4-4: u의 첫번째, 마지막 문자 제거
            tmp = tmp[1:-1]
            
            # 4-4: 괄호 방향 뒤집기
            new_tmp = ''
            for s in tmp:
                if s == '(':
                    new_tmp += ')'
                else:
                    new_tmp += '('
            
            # 4-5 반환
            return result + new + new_tmp
        
        # 3. 올바른 괄호 문자열
        else:
            return dfs(dq, result + tmp)

    return dfs(dq, '')