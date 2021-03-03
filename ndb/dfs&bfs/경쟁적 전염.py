

# X
def solution(n, k, data, s, target_x, target_y):
    
    q = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(n):
        for j in range(n):
            if data[i][j] != 0:
                q.append((data[i][j], 0, i, j))

    q.sort()

    while q:
        virus, time, x, y = q.pop(0)
        if time == s:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and data[nx][ny] == 0:
                data[nx][ny] = virus
                q.append((virus, time + 1, nx, ny))

    print(data[target_x-1][target_y-1])


solution(3, 3,  # 3
          [[1, 0, 2],
           [0, 0, 0],
           [3, 0, 0]],
          2, 3, 2)
solution(3, 3, # 0
          [[1, 0, 2],
           [0, 0, 0],
           [3, 0, 0]],
          1, 2, 2)
