from collections import deque

INF = int(1e9)
size = 2
start_x, start_y = 0, 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]
result = 0
ate = 0
data = []

n = int(input())
for i in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            start_x, start_y = i, j
            data[start_x][start_y] = 0

def bfs():
    global size
    global start_x, start_y
    dist = [[-1]*n for _ in range(n)]
    q = deque([(start_x,start_y)])
    dist[start_x][start_y] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if dist[nx][ny]==-1 and data[nx][ny]<=size:
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx,ny))
    return dist

def find(dist):
    global size
    x,y = 0,0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            if dist[i][j]!=-1 and 0<data[i][j]<size:
                if dist[i][j]<min_dist:
                    x,y=i,j
                    min_dist = dist[i][j]
    if min_dist==INF:
        return None
    else:
        return x,y,min_dist

while True:
    value = find(bfs())
    if value is None:
        print(result)
        break
    else:
        start_x, start_y = value[0], value[1]
        result += value[2]
        data[start_x][start_y] = 0
        ate += 1
        if ate>=size:
            size+=1
            ate=0