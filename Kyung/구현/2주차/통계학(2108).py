from collections import defaultdict
import sys

n = int(input())
num = list(int(sys.stdin.readline()) for _ in range(n))

num.sort()


if sum(num) > 0 :
    print(int(sum(num)/len(num) +0.5))  # 산술평균
else :
    print(int(sum(num)/len(num) -0.5))

print(num[len(num)//2])   # median

# 최빈값
d = defaultdict(int)  
for k in num :
    d[k] += 1

a = list(idx for idx, val in d.items() if val == max(d.values()))
if len(a) == 1 :
    print(a[0])
else :
    a.sort()
    print(a[1])

print(max(num)-min(num)) # 범위
