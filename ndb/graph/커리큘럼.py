
n = int(input())
indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
time = [0]*(n+1)
for i in range(1,n+1):
    a = list(map(int, input().split()))
    time[i] = a[0]
    for prev in a[1:-1]:
        indegree[i] += 1
        graph[prev].append(i)

q = []
for i in range(1,n+1):
    if indegree[i]==0:
        q.append(i)

while q:
    now = q.pop(0)
    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            time[nxt] += time[now]
            q.append(nxt)
for i in range(1, n+1):
    print(time[i])