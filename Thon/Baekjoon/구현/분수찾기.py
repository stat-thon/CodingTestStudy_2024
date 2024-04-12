### 분수찾기
# 고민: 10분
# 코딩: 21분

x = int(input())

n = 1
SUM = 1

while SUM < x:
    n += 1
    SUM = n * (n + 1) / 2


if n % 2 == 0:

    numerator = int(x - n * (n - 1) / 2)
    denominator = int(n + 1 - numerator)

    print(f'{numerator}/{denominator}')

else:

    denominator = int(x - n * (n - 1) / 2)
    numerator = int(n + 1 - denominator)

    print(f'{numerator}/{denominator}')