### 2112 - 센서
# 고민: 30분
# 코딩: 10분

N = int(input()) # 센서 수
K = int(input()) # 집중국 수
coord = list(map(int, input().split())) # 센서의 좌표

def solution(N, K, coord):

    if N == 1:
        return 0
        
    coord = sorted(list(set(coord)))
    n = len(coord) # 중복을 제거했기 때문에 N 사용 하지 않고 새로
    dist = []

    for a, b in zip(coord[:n - 1], coord[1:]):
        dist.append(b - a)

    while K - 1:

        ind = dist.index(max(dist))
        dist[ind] = 0

        K -= 1

    return sum(dist)

print(solution(N, K, coord))

### 다른 답안
N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()

sensors_diff = [sensors[i]-sensors[i-1] for i in range(1, N)]
sensors_diff.sort()

print(sum(sensors_diff[:N-K]))