### 요세푸스 문제
# 고민: 20분
# 코딩: 10분


n, k = map(int, input().split())

p = [i + 1 for i in range(n)]

result = []

for _ in range(n):
    
    mok, nam = divmod(k, len(p))
    
    result.append(p[nam - 1])
    
    # update
    if nam != 0:
        p = p[nam:] + p[:nam - 1]
        
    else:
        p = p[:nam - 1]
    
    
print("<", end = "")
for i in range(len(result)):
    
    if i == len(result) - 1:
        print(result[i], end = ">")
        
    else:
        print(result[i], end = ", ")
