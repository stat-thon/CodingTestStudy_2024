from collections import defaultdict
d = defaultdict(int)
num = input()
for x in num :
    if x == '9' or x == '6' :
        d['6'] += 0.5
    else :
        d[x] += 1

d['6'] = int(d['6'] + 0.5)  # ex) 1.5개 일 때, 2개로 처리해줘야 함(올림처리)
print(max(d.values()))