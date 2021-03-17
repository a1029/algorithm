import sys

n, m = map(int, input().split())
graph = [[False]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = True


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = True


result = [0]*(n+1)

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j]==True:
            result[i] += 1
            result[j] += 1

print(result.count(n-1))