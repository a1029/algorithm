
# X
def rotate(direction, c):
    if c == 'D':
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    return direction


def solution(n, k, k_array, info, info_array):
    board = [[0] * (n + 1) for _ in range(n + 1)]
    for a, b in k_array:
        board[a][b] = 1

    x, y = 1, 1
    board[x][y] = 2
    direction = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    time = 0
    index = 0
    body = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 2:
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                body.append((nx, ny))
                px, py = body.pop(0)
                board[px][py] = 0
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                body.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < info and time == info_array[index][0]:
            direction = rotate(direction, info_array[index][1])
            index += 1
    print(time)


solution(6,
          3, [[3, 4], [2, 5], [5, 3]],
          3, [[3, 'D'], [15, 'L'], [17, 'D']])
solution(10,
          4, [[1, 2], [1, 3], [1, 4], [1, 5]],
          4, [[8, 'D'], [10, 'D'], [11, 'D'], [13, 'L']])
solution(10,
          5, [[1, 5], [1, 3], [1, 2], [1, 6], [1, 7]],
          4, [[8, 'D'], [10, 'D'], [11, 'D'], [13, 'L']])
