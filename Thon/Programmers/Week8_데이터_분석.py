### [PCCE 기출문제] 10번 / 데이터 분석
# 고민: 5분
# 코딩: 5분
def solution(data, ext, val_ext, sort_by):
    
    label = ["code", "date", "maximum", "remain"]
    
    ext_ind = label.index(ext)
    
    result = []
    for d in data:
        if d[ext_ind] < val_ext:
            result.append(d)
            
    sort_ind = label.index(sort_by)
    
    result = sorted(result, key = lambda x : x[sort_ind])
    
    return result