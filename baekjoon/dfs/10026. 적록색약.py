import copy

# O
n = int(input())
data = []
for _ in range(n):
    data.append(list(input()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y, color, temp):
    temp[x][y] = "V"
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < n and 0 <= ny < n and temp[nx][ny] in color:
            dfs(nx, ny, color, temp)


result = []
area1 = 0
temp = copy.deepcopy(data)
for i in range(n):
    for j in range(n):
        if temp[i][j] == "B":
            dfs(i, j, ["B"], temp)
            area1 += 1
        if temp[i][j] == "R" or temp[i][j] == "G":
            dfs(i, j, ["R", "G"], temp)
            area1 += 1

area2 = 0
temp = copy.deepcopy(data)
for i in range(n):
    for j in range(n):
        if temp[i][j] == "B" or temp[i][j] == "G" or temp[i][j] == "R":
            dfs(i, j, [temp[i][j]], temp)
            area2 += 1

print(area2, area1)
