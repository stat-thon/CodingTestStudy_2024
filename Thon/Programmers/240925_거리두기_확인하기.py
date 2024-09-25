### 거리두기 확인하기
# 알고리즘: dfs
# 고민: 15분
# 코딩: 15분

def solution(places):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    def dfs(place, x, y, level):
    
        nonlocal visited, result
    
        if level == 2:
            return
    
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
        
            if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] == 0:
            
                if place[nx][ny] == 'P':
                    print(nx, ny, level)
                    result = False
                    return
            
                elif place[nx][ny] == 'X':
                    continue
            
                else:
                    visited[nx][ny] == 1
                    dfs(place, nx, ny, level + 1)

    
    answer = []
    
    for place in places:
        visited = [[0] * 5 for _ in range(5)]
        result = True
        
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))
        
        for x, y in people:
            visited[x][y] = 1
            dfs(place, x, y, 0)
            
            if result == False:
                break
        
        if result == True:
            answer.append(1)
        else:
            answer.append(0)
            
    return answer