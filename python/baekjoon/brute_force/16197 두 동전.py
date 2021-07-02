import collections
import sys

def bfs():
    while q:
        x1,y1,x2,y2,count = q.popleft()

        if count>=10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]
            if 0<=nx1<n and 0<=ny1<m and 0<=nx2<n and 0<=ny2<m:
                if d[nx1][ny1]=='#':
                    nx1,ny1 = x1,y1
                if d[nx2][ny2]=='#':
                    nx2,ny2 = x2,y2
                q.append([nx1,ny1,nx2,ny2,count+1])
            elif 0<=nx1<n and 0<=ny1<m:
                return count+1
            elif 0<=nx2<n and 0<=ny2<m:
                return count+1
            else:
                continue
    return -1

n,m = map(int, sys.stdin.readline().rstrip().split())
d = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
coin = []
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for i in range(n):
    for j in range(m):
        if d[i][j]=='o':
            coin.append((i,j))
q = collections.deque()
q.append([coin[0][0],coin[0][1],coin[1][0],coin[1][1],0])
print(bfs())