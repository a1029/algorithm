import heapq
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
start, end = map(int, input().split())
dist = [int(1e9)]*(n+1)

q = []
dist[start] = 0
heapq.heappush(q, (dist[start], start))
while q:
    v,u = heapq.heappop(q)
    if v > dist[u]:
        continue
    for w,e in graph[u]:
        cost = v + e
        if cost < dist[w]:
            dist[w] = cost
            heapq.heappush(q, (cost, w))
print(dist[end])