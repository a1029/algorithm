import heapq

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dist = [int(1e9)]*(n+1)
start = 1
dist[start] = 0
q = [(dist[start], start)]

while q:
    distance, node = heapq.heappop(q)
    if dist[node] < distance:
        continue
    for nxt in graph[node]:
        cost = distance + 1
        if cost < dist[nxt]:
            dist[nxt] = cost
            heapq.heappush(q, (cost, nxt))
max_dist = 0
max_node = 0
for i in range(1,n+1):
    if max_dist < dist[i] < int(1e9):
        max_dist = dist[i]
        max_node = i
same_count = dist.count(max_dist)
print(max_node, max_dist, same_count)