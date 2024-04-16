size = 10000
ch = [0]*(size+1)

for i in range(1, len(ch)) :
    tmp = i   # tmp는 d(n)을 만들 그릇 (어차피 자기 자신 더해야하므로 현재 숫자 i로 초기화)
    st = list(map(int,str(i)))   # 각 자리수 합을 위해 문자열 변환
    
    # 각 자리수 합
    k = 0
    while k < len(st) :   # 각 자리수 합을 위해 리스트 st에 인덱스 접근(k)
        tmp += st[k]      
        k += 1
    
    if tmp > size :  # 인덱스 범위 에러 방지
        continue    
    
    ch[tmp] = 1    # 현재 숫자 i에 대한 d(i)를 ch에 1 기입

    # 어차피 d(i)는 현재 i보다 큰 수이므로 현 숫자 i에 대해 ch[i]가 0이면 셀프 넘버  
    if ch[i] == 0 :    
        print(i)


'''

# 참고용) 다른 사람 정답
dp = [1] * 10001
for i in range(1,10001):
	d = i
	while i >0:
		d = d + i%10
		i = i//10
	d = d + i
	if d <=10000:
		dp[d] = 0
for i in range(1,10001):
	if dp[i] == 1:
		print(i)
    
'''