
import sys
from collections import deque


n, m = map(int, input().split())
graph = [[]*(n+1) for _ in range(n+1)]
indegree = [0]*(n+1)
for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    indegree[b] += 1


result = []
q = deque()
for i in range(1, n+1):
    if indegree[i]==0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

for a in result:
    print(a, end=' ')