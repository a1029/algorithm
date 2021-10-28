import sys

for _ in range(int(input())):
    n = int(input())
    last_rank = list(map(int, sys.stdin.readline().rstrip().split()))
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0]*(n+1)
    for i in range(n):
        for j in range(i+1,n):
            graph[last_rank[i]][last_rank[j]] = True
            indegree[last_rank[j]] += 1
    m = int(input())
    for _ in range(m):
        a,b = map(int, sys.stdin.readline().rstrip().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -=1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    q = []
    result = []
    for i in range(1,n+1):
        if indegree[i]==0:
            q.append(i)

    cycle = False
    certian = True
    for i in range(n):
        if len(q)==0:
            cycle = True
            break
        if len(q)>=2:
            certian = False
            break
        now = q.pop(0)
        result.append(now)
        for j in range(1,n+1):
            if graph[now][j]:
                indegree[j]-=1
                if indegree[j]==0:
                    q.append(j)
    if cycle:
        print("IMPOSSIBLE")
    elif not certian:
        print("?")
    else:
        for x in result:
            print(x, end=' ')
        print()