### n진수 게임
# 수학, 문자열
# 고민: 15분
# 코딩: 10분

def solution(n, t, m, p):
    num_dict = {i : str(i) for i in range(10)}
    
    for i in range(10, 16):
        num_dict[i] = chr(i + 55)

    make_arr = '0'
    for i in range(1, t*m):
        s = ''
        while i:
            i, nam = divmod(i, n)
            s = num_dict[nam] + s
            
        make_arr += s
            
    return make_arr[p-1::m][:t]