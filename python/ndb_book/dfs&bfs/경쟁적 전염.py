import collections
import sys
n,k = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
s,x,y = map(int, input().split())
virus = []
for i in range(n):
    for j in range(n):
        if arr[i][j]!=0:
            virus.append([i,j,arr[i][j],0])
dx = [0,1,0,-1]
dy = [1,0,-1,0]
virus.sort(key=lambda x: x[2])
q = collections.deque(virus)
while q:
    i,j,index,time = q.popleft()
    if time==s:
        break
    for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny]==0:
            arr[nx][ny]=index
            q.append([nx,ny,index,time+1])
print(arr[x-1][y-1])