import sys
import collections

n = int(sys.stdin.readline().rstrip())
graph = collections.defaultdict(list)
time = [0]*(n+1)
indegree = [0]*(n+1)
for i in range(1, n+1):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    time[i] = data[0]
    for a in data[1:-1]:
        indegree[i] += 1
        graph[a].append(i)

result = [0]*(n+1)
q = collections.deque()
for i in range(1, n+1):
    if indegree[i]==0:
        q.append(i)
        result[i] = time[i]

while q:
    now = q.popleft()
    for nxt in graph[now]:
        result[nxt] = max(result[nxt], result[now]+time[nxt])
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

for i in range(1, n+1):
    print(result[i])