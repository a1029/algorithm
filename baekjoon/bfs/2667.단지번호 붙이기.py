from collections import deque


# O
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

result = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(i, j):
    q = deque([(i,j)])
    count = 1
    while q:
        x, y = q.popleft()
        data[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] == 1:
                    q.append((nx, ny))
                    data[nx][ny] = 0
                    count += 1

    return count


for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
for n in result:
    print(n)