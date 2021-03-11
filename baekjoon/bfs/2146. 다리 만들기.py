import collections
import sys

sys.setrecursionlimit(10000)
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

visit = [[0] * n for _ in range(n)]


def labeling(x, y, label):

    data[x][y] = label
    visit[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if data[nx][ny] and not visit[nx][ny]:
                labeling(nx, ny, label)


label = 1
for i in range(n):
    for j in range(n):
        if data[i][j] and not visit[i][j]:
            labeling(i, j, label)
            label += 1


def bfs(index):

    q = collections.deque()
    for i in range(n):
        for j in range(n):
            if data[i][j] == index:
                visit[i][j] = 0
                q.append((i, j))

    dist = 0
    while q:
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if data[nx][ny] != 0 and data[nx][ny] != index:
                        return dist
                    elif data[nx][ny] == 0 and visit[nx][ny] == -1:
                        q.append((nx, ny))
                        visit[nx][ny] = 0
        dist += 1



result = 1e9
for index in range(1, label):
    for i in range(n):
        for j in range(n):
            visit[i][j] = -1
    result = min(result, bfs(index))

print(result)