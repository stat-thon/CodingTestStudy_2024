import sys

k = int(input())
tmp = []

for _ in range(k) :
    n = int(sys.stdin.readline())   # input 쓰는 습관 고치자
    if n == 0 :
        tmp.pop()
    else :
        tmp.append(n)

print(sum(tmp))