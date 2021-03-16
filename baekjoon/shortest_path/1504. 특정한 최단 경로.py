import sys
import heapq
from collections import defaultdict


def dijkstra(start):

    q = []
    dist = [1e9]*(n+1)
    dist[start] = 0
    heapq.heappush(q, (dist[start], start))
    while q:
        now = heapq.heappop(q)
        for v, w in graph[now[1]]:
            cost = now[0] + w
            if dist[v] > cost:
                dist[v] = cost
                heapq.heappush(q, (cost, v))

    return dist


graph = defaultdict(list)
n, e = map(int, input().split())
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
p1, p2 = map(int, input().split())

path1 = dijkstra(1)[p1] + dijkstra(p1)[p2] + dijkstra(p2)[n]
path2 = dijkstra(1)[p2] + dijkstra(p2)[p1] + dijkstra(p1)[n]
ans = min(path1, path2)
if ans >= 1e9:
    print(-1)
else:
    print(ans)
