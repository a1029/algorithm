
n = int(input())
arr = [[0]*n for _ in range(n)]

for _ in range(int(input())):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 2

info = []
for _ in range(int(input())):
    a, b = input().split()
    info.append((int(a),b))


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y, direct = 0, 0, 0
result = 0
body = [[0, 0]]
while True:
    nx = x+dx[direct]
    ny = y+dy[direct]
    if nx < 0 or nx >= n or ny < 0 or ny >= n or arr[nx][ny] == 1:
        print(result+1)
        break

    if arr[nx][ny] == 0:
        arr[nx][ny] = 1
        body.append([nx, ny])
        px, py = body.pop(0)
        arr[px][py] = 0
    elif arr[nx][ny] == 2:
        arr[nx][ny] = 1
        body.append([nx, ny])

    result += 1
    x, y = nx, ny
    for a, b in info:
        if result == a and b == 'L':
            direct -= 1
            if direct == -1:
                direct = 3
        elif result == a and b == 'D':
            direct += 1
            if direct == 4:
                direct = 0
