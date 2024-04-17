### 스택
# 고민: 2분
# 코딩: 20분


def push(stack, n):
    stack.append(n)
    return stack

def pop(stack):
    
    if stack:
        q = stack.pop()
        return q
    
    else:
        return -1

def size(stack):
    return len(stack)

def empty(stack):

    if stack:
        return 0
    else:
        return 1
    
def top(stack):

    if stack:
        return stack[-1]
    
    else:
        return -1
    

stack = []

def do(order):
    if order.split()[0] == 'push':
        push(stack, order.split()[1])

    elif order.split()[0] == 'pop':
        print(pop(stack))

    elif order.split()[0] == 'size':
        print(size(stack))

    elif order.split()[0] == 'empty':
        print(empty(stack))

    elif order.split()[0] == 'top':
        print(top(stack))
    
    else:
        pass

    return
        


n = int(input())

import sys

for i in range(n):
    order = sys.stdin.readline()
    do(order)

