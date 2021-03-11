import copy
import itertools
import collections

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

sea = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 0:
            sea.append([i, j])

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def labeling(i, j, label):
    q = collections.deque([(i, j)])
    data[i][j] = label
    while q:
        x, y = q.popleft()
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 1:
                data[nx][ny] = label
                q.append((nx, ny))


label = 2
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            labeling(i, j, label)
            label += 1

edges = []

for i in range(2, label + 1):
    for x in range(n):
        for y in range(n):
            if data[x][y] == i:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 0:
                        edges.append([x, y, i])
                        break



def bfs():
    result = 1e9
    visit = [[1e9] * n for _ in range(n)]
    q = collections.deque(edges)
    while q:
        x, y, label = q.popleft()
        print(q)
        visit[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if data[nx][ny] == 0 and visit[nx][ny] == 1e9:
                    visit[nx][ny] = min(visit[nx][ny], visit[x][y] + 1)
                    q.append([nx, ny, label])
                elif data[nx][ny] != 0 and data[nx][ny] != label:
                    result = min(result, visit[x][y] + 1)
                    break
        for i in range(n):
            for j in range(n):
                visit[i][j] = 1e9

    print(result)


bfs()
