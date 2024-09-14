### 방문 길이
# 구현
# 고민: 7분
# 코딩: 8분

def solution(dirs):
    
    dir = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    
    x, y = 0, 0
    visited = set()
    
    for d in dirs:
        dx, dy = dir[d]
        
        nx, ny = x + dx, y + dy
        if (-5 <= nx <= 5) and (-5 <= ny <= 5):
        
            sorted_x = tuple(sorted((x, nx)))
            sorted_y = tuple(sorted((y, ny)))
            
            if (sorted_x, sorted_y) not in visited:
            
                visited.add((sorted_x, sorted_y))
            
            x, y = nx, ny
    
    return len(visited)