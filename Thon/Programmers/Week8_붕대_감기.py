### [PCCP 기출문제] 1번 / 붕대 감ㄱ
# 고민: 19분
# 코딩: 6분

def solution(bandage, health, attacks):
    
    t, x, y = bandage
    
    # 초기화
    now = 0
    hp = health
    
    # 반복
    while attacks:
        
        attack_t, damage = attacks.pop(0) # popleft
        
        # 1. 회복
        heal_t = attack_t - now - 1 # 현재 시각을 포함하는 1초는 빼야함
        m, n = divmod(heal_t, t)
        heal_am = m * (t * x + y) + n * x # 전체 힐량
        hp = min(health, hp + heal_am)
        
        # 2. 공격
        hp -= damage
        
        if hp <= 0:
            return -1
        
        now = attack_t
    
    return hp