### 후보키
# 완전탐색
# 고민: 5분
# 코딩: 30분

def solution(relation):
    
    r, c = len(relation), len(relation[0])
    
    key_set = set()
    cand_key = set()
    
    from itertools import combinations
    for i in range(1, c + 1):
        for comb in combinations([j for j in range(c)], i):
            key_set.add(comb)
    
    # 확인
    for k in sorted(key_set, key = lambda x: (len(x))):
        check_set = set()
        
        # 최소성 확인
        cand_min = True
        for ck in cand_key:
            if set(k) & set(ck) == set(ck):
                cand_min = False
                break
        
        if not cand_min:
            continue
        
        for i in range(r):
            check_set.add(tuple(relation[i][j] for j in k))        
        
        # 유일성 확인
        if len(check_set) == r:
            cand_key.add(k)
    
    return len(cand_key)