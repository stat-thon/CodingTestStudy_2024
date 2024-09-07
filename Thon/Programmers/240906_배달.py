### 배달
# 알고리즘: 다익스트라 알고리즘, 플로이드-워셜 알고리즘
# 고민: 40분
# 코딩: 30분
# 정답 봄

# 다익스트라 알고리즘
from heapq import heappop, heappush

def dijkstra(distance, edges):
    
    heap = []
    
    # 출발 위치
    heappush(heap, (0, 1)) # 거리, 노드
    
    while heap:
        
        dist, node_in = heappop(heap)
        
        for d, node_out in edges[node_in]:
            
            # 중간노드를 거쳐간 거리 vs 직선거리
            if d + dist < distance[node_out]:
                
                distance[node_out] = d + dist
                heappush(heap, (d + dist, node_out))
                
def solution(N, road, K):
    
    # 거리 저장
    distance = [1e9 for _ in range(N + 1)]
    distance[1] = 0
    
    # 그래프 저장
    edges = [[] for _ in range(N + 1)]
    
    for i, j, d in road:
        edges[i].append((d, j))
        edges[j].append((d, i))
        
    dijkstra(distance, edges)
    
    return len([i for i in distance if i <= K])
    

# 플로이드-워셜 알고리즘
def solution(N, road, K):

    # graph를 무한값으로 초기화하여 최단 거리에서 배제할 수 있도록 함
    graph = [[int(1e9) for _ in range(N+1)] for _ in range(N + 1)]

    for i in range(1, N+1):
        graph[i][i] = 0
        
    for i, j, c in road:
        # 양방향 그래프이므로
        graph[i][j] = min(graph[i][j], c)
        graph[j][i] = min(graph[j][i], c)

    # 플로이드 워셜 알고리즘
    # k: 반드시 거쳐 지나가는 노드, i: 출발 노드, j: 도착 노드
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                # i->j 최단 거리: 기존값(graph[i][j])과 k를 지나가는 값(graph[i][k] + graph[k][j]) 중에 더 작은 값
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    ans = [x for x in graph[1] if x <=K]
    return len(ans)