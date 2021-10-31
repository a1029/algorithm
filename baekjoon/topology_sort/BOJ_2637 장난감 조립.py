import sys
import collections

n = int(input())
m = int(input())
graph = collections.defaultdict(list)
indegree = [0]*(n+1)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
    indegree[b] += 1

basic_part = []
for i in range(1, n+1):
    if not graph[i]:
        basic_part.append(i)

q = collections.deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append((i, 1))

amount = [0]*(n+1)
while q:
    now, now_need = q.popleft()
    for nxt, nxt_need in graph[now]:
        indegree[nxt] -= 1
        amount[nxt] += now_need * nxt_need
        if indegree[nxt] == 0:
            q.append((nxt, amount[nxt]))

for part in basic_part:
    print(part, amount[part])

