### ATM
# 고민: 5분
# 코딩: 1분

n = int(input())

time = list(map(int, input().split()))

cnt = 0
cnt_time = []

for p in sorted(time):
    cnt += p
    cnt_time.append(cnt)
    
print(sum(cnt_time))