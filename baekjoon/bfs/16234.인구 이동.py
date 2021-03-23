n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[-1] * n for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y):
    count = 1
    total = arr[x][y]
    q = [[x, y]]
    visit[x][y] = 0
    united = [[x,y]]
    while q:
        x, y = q.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] == -1 and l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                    visit[nx][ny] = 0
                    total += arr[nx][ny]
                    count += 1
                    q.append([nx, ny])
                    united.append([nx,ny])
    for i, j in united:
        arr[i][j] = total // count

result = 0
while True:
    tmp = 0
    visit = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == -1:
                bfs(i, j)
                tmp += 1
    if tmp == n*n:
        break
    else:
        result += 1
print(result)
