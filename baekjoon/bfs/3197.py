from collections import deque
from sys import stdin

input = stdin.readline
ex, ey, time = 0, 0, 0
dx, dy = [0,1,0,-1],[1,0,-1,0]
r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]
wc = [[False]*c for _ in range(r)]
sc = [[False]*c for _ in range(r)]
wq1, wq2 = deque(), deque()
sq1, sq2 = deque(), deque()

def water():
    while wq1:
        x, y = wq1.popleft()
        arr[x][y] = '.'
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and not wc[nx][ny]:
                if arr[nx][ny] == '.':
                    wq1.append((nx,ny))
                else:
                    wq2.append((nx,ny))
                wc[nx][ny] = True

def swan():
    while sq1:
        x, y = sq1.popleft()
        if x == ex and y == ey:
            return True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < r and 0 <= ny < c and not sc[nx][ny]:
                if arr[nx][ny] == '.':
                    sq1.append((nx, ny))
                else:
                    sq2.append((nx, ny))
                sc[nx][ny] = True
    return False

for i in range(r):
    for j in range(c):
        if arr[i][j] == 'L':
            if not sq1:
                sq1.append((i, j))
                sc[i][j] = True
            else:
                ex, ey = i, j
            arr[i][j] = '.'
        if arr[i][j] == '.':
            wq1.append((i, j))
            wc[i][j] = True
while True:
    water()
    if swan():
        break
    wq1 = wq2
    sq1 = sq2
    wq2 = deque()
    sq2 = deque()
    time += 1
print(time)
