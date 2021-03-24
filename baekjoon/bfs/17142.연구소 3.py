from itertools import combinations
from collections import deque
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
virus = []
notwall = 0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
result = 1000000000
for i in range(n):
    for j in range(n):
        if arr[i][j]==2:
            virus.append([i,j])
        if arr[i][j] != 1:
            notwall += 1
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] == 0 and arr[nx][ny] != 1:
                    visit[nx][ny] = 1
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])
cases = list(combinations(virus, m))
for case in cases:
    q = deque()
    visit = [[0]*n for _ in range(n)]
    dist = [[-1]*n for _ in range(n)]
    for x,y in case:
        q.append([x,y])
        visit[x][y] = 1
        dist[x][y] = 0
    bfs()
    infected = 0
    for i in visit:
        infected += i.count(1)
    if infected==notwall:
        time = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j]!=1 and [i,j] not in virus:
                    time = max(time, dist[i][j])
        result = min(result, time)
print(result if result!=1000000000 else -1)