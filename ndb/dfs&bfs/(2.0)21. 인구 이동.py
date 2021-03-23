import collections


def solution(n, l, r, data):
    result = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def bfs(x, y, index):

        united = []
        united.append((x, y))
        q = collections.deque()
        q.append((x, y))
        visit[x][y] = index
        summary = data[x][y]
        count = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == -1:
                    if l <= abs(data[nx][ny] - data[x][y]) <= r:
                        q.append((nx, ny))
                        visit[nx][ny] = index
                        summary += data[nx][ny]
                        count += 1
                        united.append((nx, ny))
        for i, j in united:
            data[i][j] = summary // count

    while True:
        visit = [[-1] * n for _ in range(n)]
        index = 0
        for i in range(n):
            for j in range(n):
                if visit[i][j] == -1:
                    bfs(i, j, index)
                    index += 1
        if index == n * n:
            break
        result += 1

    print(result)


solution(2, 20, 50,  # 1
         [[50, 30],
          [20, 40]])
solution(2, 40, 50,  # 0
         [[50, 30],
          [20, 40]])
solution(2, 20, 50,  # 1
         [[50, 30],
          [30, 40]])
solution(3, 5, 10,  # 2
         [[10, 15, 20],
          [20, 30, 25],
          [40, 22, 10]])
solution(4, 10, 50,  # 3
         [[10, 100, 20, 90],
          [80, 100, 60, 70],
          [70, 20, 30, 40],
          [50, 20, 100, 10]])
