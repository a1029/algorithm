import collections
import heapq


n,m,c = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    q,w,e = map(int, input().split())
    graph[q].append([w,e])
dist = [int(1e9)]*(n+1)
dist[c] = 0
q = []
heapq.heappush(q, (dist[c], c))
while q:
    d,now = heapq.heappop(q)
    if dist[now] < d:
        continue
    for nxt,nxt_d in graph[now]:
        cost = dist[now] + nxt_d
        if cost < dist[nxt]:
            dist[nxt] = cost
            heapq.heappush(q, (dist[nxt], nxt))

a,b=0,0
for i in range(1, n+1):
    if dist[i] != int(1e9) and dist[i] != 0:
        a = max(a, dist[i])
        b += 1
print(b,a)