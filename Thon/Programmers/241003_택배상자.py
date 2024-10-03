def solution(order):
    
    from collections import deque
    n = len(order)
    order = deque(order)
    belt = deque([i+1 for i in range(n)])
    result = []
    conv = deque()
    
    while belt or (conv and conv[-1] == order[0]):
        if conv and conv[-1] == order[0]:
            result.append(conv.pop())
            order.popleft()
        elif belt[0] == order[0]:
            result.append(belt.popleft())
            order.popleft()
        else:
            conv.append(belt.popleft())
            
    return len(result)