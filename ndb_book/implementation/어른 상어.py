
n,m,k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
directions = list(map(int, input().split()))
smell = [[[0,0]]*n for _ in range(n)]
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def smell_update():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1]>0:
                smell[i][j][1]-=1
            if arr[i][j]>0:
                smell[i][j] = [arr[i][j],k]

def move_shark():
    new_array = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if arr[x][y]!=0:
                direction = directions[arr[x][y]-1]
                found = False
                for index in range(4):
                    nx = x + dx[priorities[arr[x][y]-1][direction-1][index]-1]
                    ny = y + dy[priorities[arr[x][y]-1][direction-1][index]-1]
                    if 0<=nx<n and 0<=ny<n and smell[nx][ny][1]==0:
                        directions[arr[x][y]-1] = priorities[arr[x][y]-1][direction-1][index]
                        if new_array[nx][ny]==0:
                            new_array[nx][ny] = arr[x][y]
                        else:
                            new_array[nx][ny] = min(new_array[nx][ny], arr[x][y])
                        found = True
                        break
                if found:
                    continue
                for index in range(4):
                    nx = x + dx[priorities[arr[x][y]-1][direction-1][index]-1]
                    ny = y + dy[priorities[arr[x][y]-1][direction-1][index]-1]
                    if 0<=nx<n and 0<=ny<n and smell[nx][ny][0]==arr[x][y]:
                        directions[arr[x][y]-1] = priorities[arr[x][y]-1][direction-1][index]
                        new_array[nx][ny] = arr[x][y]
                        break
    return new_array

time = 0
while True:
    smell_update()
    arr = move_shark()
    time += 1
    check = True
    for i in range(n):
        for j in range(n):
            if arr[i][j]>1:
                check = False
    if check:
        print(time)
        break
    if time>=1000:
        print(-1)
        break

