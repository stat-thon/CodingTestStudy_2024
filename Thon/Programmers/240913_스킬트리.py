### 스킬트리
# 큐
# 고민: 5분
# 코딩: 15분

def solution(skill, skill_trees):
    cnt = 0
    for tree in skill_trees:
        skill_list = list(skill)
        check = [t for t in tree if t in skill]
        
        skill_success = True
        while check:
            if skill_list.pop(0) != check.pop(0):
                skill_success = False
                break
        
        if skill_success == True:
            cnt += 1
    
    return cnt 