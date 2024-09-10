### 파일명 정렬
# 문자열, 정렬
# 고민 : 10분
# 코딩 : 40분
# 일부 케이스에서 헤매다가 힌트 보고나서 실수 깨달음

def solution(files):
    
    numbers = [str(i) for i in range(10)]
    new_files = []

    for file in files:
        
        file_list = list(file)
        
        # HEAD
        HEAD = ''
        while file_list:
            
            s = file_list.pop(0)
            
            if s in numbers:
                NUMBER = s
                break

            HEAD += s.lower()
        
        # NUMBER
        while file_list:
            
            s = file_list.pop(0)
            
            if s not in numbers:
                break
            
            NUMBER += s
        
        NUMBER = NUMBER.zfill(5)
        
        # append
        new_files.append([file, HEAD, NUMBER])
    
    print(new_files)
    new_files = sorted(new_files, key = lambda x: (x[1], x[2]))
    result = [a for a, b, c in new_files]
    
    return result