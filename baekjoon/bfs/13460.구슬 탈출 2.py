n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
check = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
rx, ry, bx, by = 0, 0, 0, 0
q = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'R':
            rx, ry = i, j
        if arr[i][j] == 'B':
            bx, by = i, j

check[rx][ry][bx][by] = True
q.append((rx, ry, bx, by, 0))


def move(x, y, dx, dy, c):
    while arr[x + dx][y + dy] != '#' and arr[x][y] != 'O':
        x += dx
        y += dy
        c += 1
    return x, y, c


def bfs():
    while q:
        rx, ry, bx, by, d = q.pop(0)
        if d >= 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = move(bx, by, dx[i], dy[i], 0)
            if arr[nbx][nby] == 'O':
                continue
            if arr[nrx][nry] == 'O':
                print(d+1)
                return
            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx, nry = nrx - dx[i], nry - dy[i]
                else:
                    nbx, nby = nbx - dx[i], nby - dy[i]
            if not check[nrx][nry][nbx][nby]:
                check[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, d + 1))
    print(-1)

bfs()
