### 프로그래머스 - 삼각 달팽이
# 구현
# 고민 : 40분
# 코딩 : 15분

def solution(n):
    
    all_num = n * (n + 1) // 2
    result = [0]
    
    left, bottom, right = n % 3, (n - 1) % 3, (n - 2) % 3
    print(left, bottom, right)
    
    # floor 판단
    floordict = {}
    floor, cnt = 1, 0
    for i in range(all_num):
        
        floordict[i] = floor
        cnt += 1
        if cnt == floor:
            floor += 1
            cnt = 0
            
    # while
    while n:
        
        if n % 3 == left:
            cnt = floordict[result[-1]]
            if cnt == 1:
                for i in range(1, n):
                    result.append(result[-1] + cnt)
                    cnt += 1
            else:
                for i in range(n):
                    result.append(result[-1] + cnt)
                    cnt += 1
        
        elif n % 3 == bottom:
            for i in range(n):
                result.append(result[-1] + 1)
        
        else:
            floor = floordict[result[-1]]
            for i in range(n):
                result.append(result[-1] - floor)
                floor -= 1
        
        n -= 1
    
    answer = [0] * all_num
    for i, c in enumerate(result):
        answer[c] = i + 1
    
    return answer