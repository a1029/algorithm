from copy import deepcopy
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
zero_list = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            zero_list.append([i, j])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(temp):
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 2:
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for direction in range(4):
                        nx = x + dx[direction]
                        ny = y + dy[direction]
                        if 0 <= nx < n and 0 <= ny < m and temp[nx][ny] == 0:
                            temp[nx][ny] = 2
                            q.append((nx, ny))
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    return count

result = 0
for case in list(combinations(zero_list, 3)):
    temp = deepcopy(data)
    for x, y in case:
        temp[x][y] = 1
    result = max(result, bfs(temp))
print(result)