def turn_left():
    global d
    d -= 1
    if d < 0:
        d = 3

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visit = [[0] * m for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visit[r][c] = 1
count = 0
result = 1
while True:
    turn_left()
    nx = r + dx[d]
    ny = c + dy[d]
    count += 1
    if 0 <= nx < n and 0 <= ny < m:
        if visit[nx][ny] == 0 and arr[nx][ny] == 0:
            visit[nx][ny] = 1
            r = nx
            c = ny
            count = 0
            result += 1
    if count >= 4:
        nx = r - dx[d]
        ny = c - dy[d]
        if arr[nx][ny] == 1:
            break
        else:
            r = nx
            c = ny
            count = 0

print(result)
