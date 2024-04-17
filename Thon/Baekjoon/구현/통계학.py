### 통계학
# 고민: 1분
# 코딩: 15분

import sys

n = int(input())

num = []

for _ in range(n):
    num.append(int(sys.stdin.readline()))

num = sorted(num)

mean = round(sum(num) / len(num))
median = num[len(num) // 2]
from collections import Counter

MAX, MAX_list = 0, []
for k, v in Counter(num).items():

    if v > MAX:
        MAX = v
        MAX_list = [k]

    elif v == MAX:
        MAX_list.append(k)

    else:
        pass

def mode(MAX_list):

    if len(MAX_list) > 1:
        return sorted(MAX_list)[1]

    else:
        return MAX_list[0]
        


ran = num[-1] - num[0]
print(mean, median, mode(MAX_list), ran, sep = "\n")