
# O
n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

visit = [[-1] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = [(0, 0)]
visit[0][0] = 0

while q:
    x, y = q.pop(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if data[nx][ny] == 1 and visit[nx][ny] == -1:
                visit[nx][ny] = 0
                data[nx][ny] = data[x][y] + 1
                q.append((nx, ny))

print(data[n - 1][m - 1])
