### 9465 - 스티커
# 고민: 30분
# 코딩: 포기

import sys
input = sys.stdin.readline

T = int(input())

def solution(stickers, n):

    DP[0][0] = stickers[0][0]
    DP[1][0] = stickers[1][0]
    
    if n == 1:
        return max(DP[0][0], DP[1][0])

    DP[0][1] = stickers[1][0] + stickers[0][1]
    DP[1][1] = stickers[0][0] + stickers[1][1]

    if n == 2:
        return max(DP[0][1], DP[1][1])
        
    for i in range(2, n):

        DP[0][i] = max(DP[1][i - 2], DP[1][i - 1]) + stickers[0][i]
        DP[1][i] = max(DP[0][i - 2], DP[0][i - 1]) + stickers[1][i]

    return max(DP[0][-1], DP[1][-1])
        


for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    DP = [[0] * n for _ in range(2)]
    print(solution(stickers, n))
    


