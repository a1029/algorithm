import heapq


# success
def my_answer(n, data):
    inf = int(1e9)
    dist = [[inf] * n for _ in range(n)]
    visit = [[-1] * n for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    dist[0][0] = data[0][0]
    visit[0][0] = 0
    q = [(dist[0][0], 0, 0)]

    while q:
        d, x, y = heapq.heappop(q)
        visit[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == -1:
                cost = d + data[nx][ny]
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

    print(dist[n - 1][n - 1])


my_answer(3, [[5, 5, 4],
              [3, 9, 1],
              [3, 2, 7]])
my_answer(5, [[3, 7, 2, 0, 1],
              [2, 8, 0, 9, 1],
              [1, 2, 1, 8, 1],
              [9, 8, 9, 2, 0],
              [3, 6, 5, 1, 5]])
my_answer(7, [[9, 0, 5, 1, 1, 5, 3],
              [4, 1, 2, 1, 6, 5, 3],
              [0, 7, 6, 1, 6, 8, 5],
              [1, 1, 7, 8, 3, 2, 3],
              [9, 4, 0, 7, 6, 4, 1],
              [5, 8, 3, 2, 4, 8, 3],
              [7, 4, 8, 4, 8, 3, 4]])
