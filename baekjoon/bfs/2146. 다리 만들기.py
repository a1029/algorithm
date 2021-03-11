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


def get_edge(label):
    edges = []
    for x in range(n):
        for y in range(n):
            if data[x][y] == label:
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 0:
                        edges.append([x, y])
    if edges:
        return edges
    else:
        return None

label = 2
for i in range(n):
    for j in range(n):
        edges = get_edge(label)
        bfs(edges, label)
