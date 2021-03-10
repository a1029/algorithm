import sys

# O
r, c = map(int, input().split())
data = []
for i in range(r):
    data.append(list(map(lambda x: ord(x)-65, sys.stdin.readline().rstrip())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 0
visit = [0]*26
visit[data[0][0]] = 1


def dfs(x, y, count):
    global result
    global visit

    result = max(result, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and visit[data[nx][ny]] == 0:
            visit[data[nx][ny]] = 1
            dfs(nx, ny, count + 1)
            visit[data[nx][ny]] = 0


dfs(0, 0, 1)
print(result)
