### 메뉴 리뉴얼
# 완전탐색
# 고민: 30분
# 코딩: 30분

def solution(orders, course):
    
    from itertools import combinations
    from collections import defaultdict
    
    n = len(orders)
    count = defaultdict(set)
    
    # 조합으로 확인
    for a, b in combinations([i for i in range(n)], 2):
        inter = set(orders[a]) & set(orders[b])
        
        # 교집합 내의 조합 중에서도 확인해야 함
        for l in range(2, len(inter)+1):
            if l in course:
                for comb in combinations(inter, l):
                    s = "".join(sorted(comb))
                    count[s].add(a)
                    count[s].add(b)
    
    # 개수 세기
    result = []
    for cnt in course:
        cand = []
        MAX = 0
        for k, v in count.items():
            if len(k) == cnt:
                if len(v) > MAX:
                    cand = [k]
                    MAX = len(v)
                elif len(v) == MAX:
                    cand.append(k)
        
        result += cand
    
    return sorted(result)