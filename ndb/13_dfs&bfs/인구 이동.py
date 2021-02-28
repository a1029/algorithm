def my_answer(n, l, r, data):
    unions = []
    union = set()
    visit = [[0] * n for _ in range(n)]
    result = 0

    def bfs(x, y):

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        q = [[x, y]]
        while q:

            cx, cy = q.pop(0)
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 0 <= nx < n and 0 <= ny < n and l <= abs(data[cx][cy] - data[nx][ny]) <= r:
                    union.add((cx, cy))
                    union.add((nx, ny))
                    q.append([nx, ny])

        return union

    def update():
        a = 0
        for u in unions:
            for i, j in u:
                a += data[i][j]
            a /= len(u)
            for i, j in u:
                data[i][j] = a
            a = 0

    while True:
        for i in range(n):
            for j in range(n):
                if visit[i][j] == 0:
                    unions.append(bfs(i, j))
                    for a, b in union:
                        visit[a][b] = 1
                    union.clear()

        if len(union)==0:
            print(result)
            return
        update()
        result += 1


my_answer(2, 20, 50,
          [[50, 30],
           [20, 40]])
'''my_answer(2, 40, 50,
          [[50, 30],
           [20, 40]])
my_answer(2, 20, 50,
          [[50, 30],
           [30, 40]])
my_answer(3, 5, 10,
          [[10, 15, 20],
           [20, 30, 25],
           [40, 22, 10]])
my_answer(4, 10, 50,
          [[10, 100, 20, 90],
           [80, 100, 60, 70],
           [70, 20, 30, 40],
           [50, 20, 100, 10]])
'''