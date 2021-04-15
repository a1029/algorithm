import sys
sys.setrecursionlimit(10**6)
n,r,q = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
result = [0]*(n+1)
def dfs(root):
    result[root] = 1
    for nxt in graph[root]:
        if result[nxt]==0:
            result[root] += dfs(nxt)
    return result[root]
dfs(r)

for _ in range(q):
    print(result[int(sys.stdin.readline().rstrip())])