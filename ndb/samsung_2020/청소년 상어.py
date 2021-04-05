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

def move_all_fished(arr,now_x,now_y):
    for i in range(1,17):
        pos = find_fish(arr, i)
        if pos!=None:
            x,y=pos[0],pos[1]
            direction = arr[x][y][1]
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0<=nx<4 and 0<=ny<4:
                    if not (nx==now_x and ny==now_y):
                        arr[x][y][1] = direction
                        arr[x][y],arr[nx][ny] = arr[nx][ny],arr[x][y]
                        break
                direction = turn_left(direction)

def get_possible_pos(arr,now_x,now_y):
    positions = []
    direction = arr[now_x][now_y][1]
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if 0<=now_x<4 and 0<=now_y<4:
            if arr[now_x][now_y][0]!=-1:
                positions.append((now_x,now_y))
    return positions

def dfs(data,now_x,now_y,total):
    global result
    arr = copy.deepcopy(data)
    total += arr[now_x][now_y][0]
    arr[now_x][now_y][0] = -1
    move_all_fished(arr,now_x,now_y)
    positions = get_possible_pos(arr,now_x,now_y)
    if len(positions)==0:
        result = max(result, total)
        return
    for next_x,next_y in positions:
        dfs(arr,next_x,next_y,total)

dfs(arr,0,0,0)
print(result)