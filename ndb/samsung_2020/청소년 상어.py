import copy

arr = [[None]*4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = [data[j*2],data[j*2+1]-1]
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
result = 0

def turn_left(direction):
    return (direction+1)%8


def find_fish(arr, index):
    for i in range(4):
        for j in range(4):
            if arr[i][j][0]==index:
                return (i,j)
    return None


def move_all_fish(arr, sx, sy):
    for index in range(1,17):
        pos = find_fish(arr, index)
        if pos is not None:
            x,y = pos[0], pos[1]
            direction = arr[x][y][1]
            for _ in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0<=nx<4 and 0<=ny<4 and not (nx==sx and ny==sy):
                    arr[x][y][1] = direction
                    arr[x][y],arr[nx][ny] = arr[nx][ny], arr[x][y]
                    break
                direction = turn_left(direction)

def possible_eat_to_fish(arr, sx, sy):
    fishes = []
    direction = arr[sx][sy][1]
    for i in range(4):
        sx += dx[direction]
        sy += dy[direction]
        if 0<=sx<4 and 0<=sy<4 and arr[sx][sy][0]!=-1:
            fishes.append((sx,sy))
    return fishes

def dfs(arr, sx, sy, total):
    global result
    arr = copy.deepcopy(arr)
    total += arr[sx][sy][0]
    arr[sx][sy][0] = -1
    move_all_fish(arr, sx, sy)
    fishes = possible_eat_to_fish(arr, sx, sy)
    if not fishes:
        result = max(result, total)
        return
    for x,y in fishes:
        dfs(arr,x,y,total)

dfs(arr,0,0,0)
print(result)

