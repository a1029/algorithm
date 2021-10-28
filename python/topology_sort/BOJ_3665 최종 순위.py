import sys
import collections

test_case = int(input())
for _ in range(test_case):  
    n = int(input())
    graph = [[False]*(n+1) for _ in range(n+1)]
    indegree = [0]*(n+1)

    last = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(n):
        for j in range(i+1, n):
            graph[last[i]][last[j]] = True
            indegree[last[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1
    
    q = collections.deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    flag = 0
    result = []
    for _ in range(n):
        if len(q) == 0:
            flag = 2
            break
        if len(q) >= 2:
            flag = 1
            break
        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] <= 0:
                    q.append(j)
    
    if flag == 0:
        for a in result:
            print(a, end=' ')
        print("")
    elif flag == 1:
        print("?")
    else:
        print("IMPOSSIBLE")