import copy

# X
result = 0

def solution(m):
    data = [[None] * 4 for _ in range(4)]

    for i in range(4):
        array = m[i]
        for j in range(4):
            data[i][j] = [array[j * 2], array[j * 2 + 1] - 1]

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, -1, -1, -1, 0, 1, 1, 1]

    def turn(position):
        return (position + 1) % 8

    def find_fish(data, index):
        for i in range(4):
            for j in range(4):
                if data[i][j][0] == index:
                    return i, j
        return None

    def move(data, now_x, now_y):
        for i in range(1, 17):
            position = find_fish(data, i)
            if position is not None:
                x, y = position[0], position[1]
                direction = data[x][y][1]
                for j in range(8):
                    nx = x + dx[direction]
                    ny = y + dy[direction]
                    if 0 <= nx < 4 and 0 <= ny < 4:
                        if not (nx == now_x and ny == now_y):
                            data[x][y][1] = direction
                            data[x][y], data[nx][ny] = data[nx][ny], data[x][y]
                            break
                    direction = turn(direction)

    def get_possible_positions(data, now_x, now_y):

        positions = []
        direction = data[now_x][now_y][1]
        for i in range(4):
            now_x += dx[direction]
            now_y += dy[direction]
            if 0 <= now_x < 4 and 0 <= now_y < 4:
                if data[now_x][now_y][0] != -1:
                    positions.append((now_x, now_y))

        return positions

    def dfs(data, now_x, now_y, total):

        global result

        data = copy.deepcopy(data)

        total += data[now_x][now_y][0]
        data[now_x][now_y][0] = -1

        move(data, now_x, now_y)

        positions = get_possible_positions(data, now_x, now_y)
        if len(positions) == 0:
            result = max(result, total)
            return
        for next_x, next_y in positions:
            dfs(data, next_x, next_y, total)

    global result

    dfs(data, 0, 0, 0)
    print(result)


solution([[7, 6, 2, 3, 15, 6, 9, 8],
          [3, 1, 1, 8, 14, 7, 10, 1],
          [6, 1, 13, 6, 4, 3, 11, 4],
          [16, 1, 8, 7, 5, 2, 12, 2]])
solution([[16, 7, 1, 4, 4, 3, 12, 8],
          [14, 7, 7, 6, 3, 4, 10, 2],
          [5, 2, 15, 2, 8, 3, 6, 4],
          [11, 8, 2, 4, 13, 5, 9, 4]])
solution([[12, 6, 14, 5, 4, 5, 6, 7],
          [15, 1, 11, 7, 3, 7, 7, 5],
          [10, 3, 8, 3, 16, 6, 1, 1],
          [5, 8, 2, 7, 13, 6, 9, 2]])
