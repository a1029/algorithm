

n,m = map(int, input().split())
graph = [[int(1e9)]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

result = 0
for i in range(1, n+1):
    c = 0
    for j in range(1, n+1):
        if graph[i][j]<1e9 or graph[j][i]<1e9:
            c += 1
    if c==n:
        result += 1
print(result)
