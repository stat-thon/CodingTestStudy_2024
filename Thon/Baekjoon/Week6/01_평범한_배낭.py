### 12865 - 평범한 배낭
# 고민: 25분
# 코딩: 포기

# 참고 답안 1
import sys
input = sys.stdin.readline
n, k = map(int, input().split())

stuff = [[0,0]]
DP = [[0] * (k+1) for _ in range(n+1)]

for _ in range(n):
    stuff.append(list(map(int, input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        w,v = stuff[i]
        if j >= w:
            DP[i][j] = max(DP[i-1][j] , DP[i-1][j-w] + v)
        else:
            DP[i][j] = DP[i-1][j]

print(DP[i][k])

# 1. 냅색 알고리즘이라고 함
# 2. 물건의 개수를 행, 배낭의 용량을 열로 한 2중 배열 생성
# 3. 이중 반복을 수행하여 현재 보고있는 물건의 무게가 해당하는 열의 용량(무게)보다 크면 담을 수 없음
#    -> 이전 물건에 해당하는 knapsack[i - 1][j]를 그대로 적용
# 4. 물건의 무게가 더 가벼운 경우
#    4-1) 현재물건의 무게 + knapsack[i - 1][j - 현재물건] + v를 계산
#    4-2) 이전 물건만 담았을 때의 가치 knapsack[i - 1][j] 조회
#    4-3) 4-1, 4-2의 결과 중 최대 가치를 저장


# 시간복잡도 개선한 DP 풀이
import sys;
input = sys.stdin.readline

# 향상된 DP 풀이
def main(): # 함수화
    n, k = map(int, input().split())
    k += 1

    bag = {0: 0}
    data = [tuple(map(int,input().split())) for _ in range(n)]
    data.sort(reverse=True)

    for w, v in data:
        tmp = {}
        for v_bag, w_bag in bag.items():
            if bag.get(nv := v + v_bag, k) > (nw := w + w_bag):
                tmp[nv]=nw
        bag.update(tmp)

    print(max(bag.keys()))

main()

# := (0월러스 연산자) : 표현식 안에서 변수를 할당하는 동시에 그 값을 반환하는 코드
# 조건문 안에서 nv라는 변수로 v + v_bag을 할당하여 nv라는 변수를 반환하도록 함
# 마찬가지로, 조건문 안에서 nw라는 변수로 w + w_bag을 할당하고 nw로 반환
# .get() 메소드: 딕셔너리에서 특정 키의 값을 가져올 때 사용 -> 키가 딕셔너리 안에 존재하지 않을 때, 기본값을 반환하도록 함
#  -> get(키, 기본값) 