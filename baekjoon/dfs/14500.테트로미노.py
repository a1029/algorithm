

def dfs(x,y,prev,length):
    global result
    if length >= 4:
        result = max(result, prev)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if not check[nx][ny]:
            check[nx][ny] = 1
            dfs(nx, ny, prev+arr[nx][ny], length+1)
            check[nx][ny] = 0

def certian_check(x, y):

    global result
    for i in range(4):
        prev = 0
        flag = 0
        for j in range(4):
            nx = x + ex[i][j]
            ny = y + ey[i][j]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                flag = 1
                break
            else:
                prev += arr[nx][ny]
        if not flag:
            result = max(result, prev)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ex = [[0, 0, 0, 1], [0, 1, 2, 1], [0, 0, 0, -1], [0, -1, 0, 1]]
ey = [[0, 1, 2, 1], [0, 0, 0, 1], [0, 1, 2, 1], [0, 1, 1, 1]]
result = 0

for i in range(n):
    for j in range(m):
        check[i][j] = 1
        dfs(i, j, arr[i][j], 1)
        check[i][j] = 0
        certian_check(i, j)

print(result)