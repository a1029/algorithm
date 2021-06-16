from collections import deque
n, m = map(int, input().split())

data = []
for i in range(n):
    data.append(list(map(int, input().split())))

visit = [[0]*m for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs():

    for i in range(n):
        for j in range(m):
            visit[i][j] = 0

    q = deque([(0,0)])
    visit[0][0] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not data[nx][ny] and not visit[nx][ny]:
                    visit[nx][ny] = 1
                    q.append((nx,ny))
                elif data[nx][ny]:
                    data[nx][ny] += 1
def melt():
    for i in range(n):
        for j in range(m):
            if data[i][j] >= 3:
                data[i][j] = 0
            elif data[i][j] == 2:
                data[i][j] = 1

def check():

    for i in range(n):
        for j in range(m):
            if data[i][j] == 1:
                return False
    return True

result = 0
while True:
    bfs()
    melt()
    result += 1
    if check():
        print(result)
        break
