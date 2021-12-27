from collections import defaultdict
import heapq

# https://programmers.co.kr/learn/courses/30/lessons/12978
def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    for a,b,c in road:
        graph[a].append([b,c])
        graph[b].append([a,c])
    q = []
    dist = [1e9]*(N+1)
    dist[1] = 0
    heapq.heappush(q, (0, 1))
    while q:
        w, v = heapq.heappop(q)
        if dist[v] < w:
            continue
        for nv,nw in graph[v]:
            if w + nw < dist[nv]:
                dist[nv] = w + nw
                heapq.heappush(q, (w + nw, nv))
    for d in dist[1:]:
        if d <= K:
            answer += 1
    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))