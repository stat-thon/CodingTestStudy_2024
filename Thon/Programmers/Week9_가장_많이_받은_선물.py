### 프로그래머스 - 가장 많이 받은 선물
# 고민: 10분
# 코딩: 25분

def solution(friends, gifts):
    n = len(friends)
    presents = dict()
    presents_index = dict()
    predict = dict()
    
    for i in range(n):
        presents[friends[i]] = {friends[j]: 0 for j in range(n) if j != i}
        presents_index[friends[i]] = 0
        predict[friends[i]] = 0
    
    
    for g in gifts:
        a, b = g.split()
        
        presents[a][b] += 1
        presents_index[a] += 1
        presents_index[b] -= 1
        
    
    for a in range(n):
        for b in range(n):
            if a > b:
                A, B = friends[a], friends[b]
                if presents[A][B] > presents[B][A]: # a가 b한테 준 게 더 많으면
                    predict[A] += 1
                
                elif presents[A][B] < presents[B][A]:
                    predict[B] += 1
                    
                else: 
                    
                    if presents_index[A] > presents_index[B]:
                        predict[A] += 1
                    elif presents_index[A] < presents_index[B]:
                        predict[B] += 1
                
    
    return max(predict.values())