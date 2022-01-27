from collections import deque

m,n = map(int, input().split())
arr = [list(map(int, (input().split()))) for _ in range(n)]

d = {
    1: [0,-1],
    2: [-1,0],
    4: [0,1],
    8: [1,0]
}

count, max_area, two_area = 0, 0, 0
number = 0
visit = [[False]*m for _ in range(n)]
areas = [[-1,-1]*m for _ in range(n)]

def bfs(a,b,visit, number):
    global max_area
    q = deque()
    q.append([a,b])
    visit[a][b] = True
    area = 1
    pos = [[a,b]]
    while q:
        x,y = q.popleft()
        for i in [1,2,4,8]:
            if arr[x][y] & i == 0:
                nx = x + d[i][0]
                ny = y + d[i][1]
                if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
                    q.append([nx,ny])
                    visit[nx][ny] = True
                    area += 1
                    pos.append([nx,ny])
    
    for i,j in pos:
        areas[i][j] = [area, number]
    max_area = max(max_area, area)

    return 1

for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            count += bfs(i,j,visit, number)
            number += 1

for i in range(n):
    for j in range(m):
        for k in [1,2,4,8]:         
            ni = i + d[k][0]
            nj = j + d[k][1]
            if 0<=ni<n and 0<=nj<m and areas[i][j][1] != areas[ni][nj][1]:
                two_area = max(two_area, areas[i][j][0] + areas[ni][nj][0])

print(count, max_area, two_area)