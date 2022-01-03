import heapq
from collections import defaultdict
def solution(n, edge):
    answer = 0
    q = []
    graph = defaultdict(list)
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    dist = [1e9]*(n+1)
    dist[1] = 0
    heapq.heappush(q, (0, 1))
    while q:
        w, v = heapq.heappop(q)
        if dist[v] < w:
            continue
        for nv in graph[v]:
            nw = w + 1
            if dist[nv] > nw:
                dist[nv] = nw
                heapq.heappush(q, (dist[nv], nv))
    
    return dist.count(max(dist[1:]))