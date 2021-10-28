import sys
input = sys.stdin.readline
r,c,t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]
c1,c2 = 0,0
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for i in range(r):
    if arr[i][0]==-1:
        c1 = i
        c2 = i+1
        break

def clean():
    for i in range(c1-1,0,-1):
        arr[i][0] = arr[i-1][0]
        arr[i-1][0] = 0
    for j in range(c-1):
        arr[0][j] = arr[0][j+1]
        arr[0][j+1] = 0
    for i in range(c1):
        arr[i][c-1] = arr[i+1][c-1]
        arr[i+1][c-1] = 0
    for j in range(c-1,1,-1):
        arr[c1][j] = arr[c1][j-1]
        arr[c1][j-1] = 0

    for i in range(c2+1,r-1):
        arr[i][0] = arr[i+1][0]
        arr[i+1][0] = 0
    for j in range(c-1):
        arr[r-1][j] = arr[r-1][j+1]
        arr[r-1][j+1] = 0
    for i in range(r-1,c2,-1):
        arr[i][c-1] = arr[i-1][c-1]
        arr[i-1][c-1] = 0
    for j in range(c-1,1,-1):
        arr[c2][j] = arr[c2][j-1]
        arr[c2][j-1] = 0

def bfs():
    tmp = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if arr[x][y] >= 5:
                minus = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and arr[nx][ny]!=-1:
                        tmp[nx][ny] += arr[x][y]//5
                        minus += arr[x][y]//5
                tmp[x][y] -= minus
    for i in range(r):
        for j in range(c):
            arr[i][j] += tmp[i][j]

for _ in range(t):
    bfs()
    clean()
result = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] > 0:
            result += arr[i][j]
print(result)