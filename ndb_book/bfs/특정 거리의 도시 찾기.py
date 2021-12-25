import collections
import sys

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
dist = [int(1e9)]*(n+1)
dist[x] = 0
q = collections.deque([x])
while q:
    now = q.popleft()
    for nxt in graph[now]:
        if dist[nxt] == int(1e9):
            dist[nxt] = dist[now] + 1
            q.append(nxt)

result = []
for i,cost in enumerate(dist):
    if cost==k:
        result.append(i)
result.sort()
if not result:
    print(-1)
else:
    for index in result:
        print(index)
