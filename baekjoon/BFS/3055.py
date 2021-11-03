from collections import deque
r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
dist = [[-1]*c for _ in range(r)]
w, q = deque(), deque()
a,b=0,0
count = 0
for i in range(r):
    for j in range(c):
        if arr[i][j]=='S':
            q.append([i,j])
            arr[i][j]='.'
            dist[i][j] = 0
        if arr[i][j]=='*':
            w.append([i,j])
        if arr[i][j]=='D':
            a,b=i,j
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def flood():
    for _ in range(len(w)):
        x, y = w.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == '.':
                arr[nx][ny] = '*'
                w.append([nx, ny])
def move():
    for _ in range(len(q)):
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if (arr[nx][ny] == '.' or arr[nx][ny] == 'D') and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append([nx, ny])
while True:
    flood()
    move()
    count+=1
    if dist[a][b]!=-1:
        print(dist[a][b])
        break
    if count>=r*c:
        print("KAKTUS")
        break
