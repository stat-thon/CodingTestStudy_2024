### 트럭
# 고민: 18분
# 코딩: 2분


from collections import deque

n, w, L = map(int, input().split())

trucks = deque(map(int, input().split()))

time = 0
on_bridge = deque([0] * w)

while trucks or on_bridge:
    
    on_bridge.popleft()
    
    if trucks:
        if sum(on_bridge) + trucks[0] <= L:
            on_bridge.append(trucks.popleft())
            
        else:
            on_bridge.append(0)
            
    
    time += 1
    
print(time)