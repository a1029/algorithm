import sys
from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
low, high = 0, 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    high = max(high, c)
    graph[a].append([b,c])
    graph[b].append([a,c])
start, end = map(int, input().split())

visit = [False]*(n+1)


def bfs(limit):

    q = [start]
    visit[start] = True
    while q:
        now = q.pop(0)
        if now == end:
            return True
        for nxt, cost in graph[now]:
            if not visit[nxt] and limit <= cost:
                visit[nxt] = True
                q.append(nxt)

    return False


while low <= high:
    for i in range(n+1):
        visit[i] = False
    mid = (low+high)//2
    if bfs(mid):
        low = mid+1
    else:
        high = mid-1

print(high)
