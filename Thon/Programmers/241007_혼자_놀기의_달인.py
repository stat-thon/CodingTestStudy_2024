### 혼자 놀기의 달인
# 구현
# 고민: 15분
# 코딩: 10분

def solution(cards):
    cards = [c-1 for c in cards]
    record = [0] * len(cards)
    result = []
    
    while not all(record):          
        
        for i in range(len(cards)):
            if record[i] == 0:
                tmp = i
                break
        
        l_set = {tmp}
        
        while True:
            
            record[tmp] = 1
            tmp = cards[tmp] # next tmp
            
            if tmp in l_set:
                break
            
            l_set.add(tmp)
        
        result.append(list(l_set))
    
    result = sorted(result, key = len, reverse = True)
    
    if len(result) == 1:
        return 0
    
    return len(result[0]) * len(result[1])