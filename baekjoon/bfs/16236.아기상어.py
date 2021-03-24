from collections import deque

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

now_x, now_y = 0, 0
for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            now_x, now_y = i, j
            data[i][j] = 0

size = 2
ate = 0


def bfs():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dist = [[-1] * n for _ in range(n)]

    dist[now_x][now_y] = 0
    q = deque([(now_x, now_y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] <= size and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist


result = 0
while True:
    min_dist = 1e9
    dist = bfs()
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 1 <= data[i][j] < size:
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    now_x, now_y = i, j

    if min_dist == 1e9:
        print(result)
        break
    else:
        data[now_x][now_y] = 0
        result += dist[now_x][now_y]
        ate += 1
        if ate >= size:
            size += 1
            ate = 0