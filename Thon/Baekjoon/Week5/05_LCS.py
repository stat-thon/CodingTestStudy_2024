### 9251 - LCS
# 고민: 20분
# 코딩: 포기

# 답안 1.DP
import sys
read = sys.stdin.readline

word1, word2 = read().strip(), read().strip()
h, w = len(word1), len(word2)
cache = [[0] * (w+1) for _ in range(h+1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        if word1[i-1] == word2[j-1]:
            cache[i][j] = cache[i-1][j-1] + 1
        else:
            cache[i][j] = max(cache[i][j-1], cache[i-1][j])
print(cache[-1][-1])

# 설명
# 1. 2차원 배열로 LCS 길이 캐시값을 저장 업데이트
# 2. 이중 반복으로 확인했을 때 현 시점 i, j를 기준으로 word1[i-1] == word2[j-1]이면 같은 숫자가 있으므로 cache[i-1][j-1] 값에 1 추가한 값을 cache[i][j]에 기록
# 3. 다른 경우가 중요한데, 다르면 cache[i-1][j]와 cache[i][j-1]을 비교하여 더 큰 값을 기록
# 4. 그 이유는, 예를 들어 CAP와 ACA를 비교할 때
# - CAP는 AC까지만 볼 때 LCS가 1이지만
# - ACA는 CA를 봤을 때 LCS가 2임 -> 둘 중 최대값인 2를 써야 CAP와 ACA의 LCS가 결정됨
# 이렇게 cache를 업데이트 하고 행렬의 맨 마지막값을 출력하면 LCS가 됨



# 답안 2. 시간복잡도 개선
import sys
read = sys.stdin.readline

word1, word2 = read().strip(), read().strip()
l1, l2 = len(word1), len(word2)
cache = [0] * l2

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = cnt + 1
print(max(cache))

# 설명
# 1. cache에는  두번째 단어를 순회하면서 누적변수와 cache의 값을 비교하여 업데이트 하는 방향
# 2. 누적변수로 cnt를 써서 첫번째 단어에 저장된 cache값을 불러오고, 같은 글자면 누적변수에 1을 더한 값을 캐시에 저장
# 3. 단, 같은 글자가 나왔다고 해서 누적변수인 cnt를 업데이트 하지 않음.
# 4. 이런 방식을 사용하면, 누적변수에는 이전 위치까지의 최대값을 저장하게 됨
# 5. 최종적으로 cache에 저장된 값의 최대값을 출력
# 상당히 이해가 안 됨



# 출처
# https://myjamong.tistory.com/317