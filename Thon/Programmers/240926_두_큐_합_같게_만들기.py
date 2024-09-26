### 두 큐 합 같게 만들기
# 알고리즘: 큐
# 고민: 20분
# 코딩: 40분

def solution(q1, q2):
    
    from collections import deque
    q1, q2 = deque(q1), deque(q2)
    sum1, sum2 = sum(q1), sum(q2)
    limit = len(q1) * 2 + len(q2)
    
    cnt = 0
    
    while sum1 != sum2:
            
        if cnt == limit:
            return -1
            
        if sum1 < sum2:
            q = q2.popleft()
            q1.append(q)
            sum1 += q
            sum2 -= q
            cnt += 1
                
        else:
            q = q1.popleft()
            q2.append(q)
            sum1 -= q
            sum2 += q
            cnt += 1
                    
    return cnt