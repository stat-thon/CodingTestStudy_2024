word = input()
table = ['c=','c-','dz=','d-','lj','nj','s=','z=']
   # 주의 : 만약 dz=가 z=보다 뒤에 위치한다면 밑의 코드는 반복문 순서상 오답을 출력함 

# 예제 4번 보면 중복되는 알파벳도 개별로 취급하여 카운트함
for x in table :  # table에 포함되지 않은 알파벳도 카운트해야 함
    word = word.replace(x, '@')   # table에 있는 각 단어들은 하나의 알파벳으로 취급하므로 
                                  # 길이가 1인 문자 @로 대체
                                  # replace는 다시 담아줘야 반영됨
print(len(word))    