n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dice = [0] * 7
move = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
for i in range(k):
    nx = x + dx[move[i]]
    ny = y + dy[move[i]]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
    if move[i] == 1:
        dice[3], dice[1], dice[4], dice[6] = dice[1], dice[4], dice[6], dice[3]
    if move[i] == 2:
        dice[4], dice[1], dice[3], dice[6] = dice[1], dice[3], dice[6], dice[4]
    if move[i] == 3:
        dice[2], dice[1], dice[5], dice[6] = dice[1], dice[5], dice[6], dice[2]
    if move[i] == 4:
        dice[5], dice[1], dice[2], dice[6] = dice[1], dice[2], dice[6], dice[5]

    if arr[nx][ny] == 0:
        arr[nx][ny] = dice[6]
    else:
        dice[6] = arr[nx][ny]
        arr[nx][ny] = 0
    print(dice[1])
    x, y = nx, ny
