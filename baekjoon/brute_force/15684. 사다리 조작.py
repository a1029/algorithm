
n,m,h = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]

ladder = [[0]*(n+1) for _ in range(h+1)]
need = 0
flag = 0
for a,b in data:
    ladder[a][b] = 1


def dfs(col, laddercnt):
    global flag

    if flag:
        return

    if laddercnt == need:
        possible = True
        for i in range(1, n+1):
            row = i
            for j in range(1, h+1):
                if ladder[j][row]:
                    row += 1
                elif row > 1 and ladder[j][row-1]:
                    row -= 1
            if i != row:
                possible = False
                break
        if possible:
            flag = True
        return

    for i in range(col, h+1):
        for j in range(1, n):
            if not ladder[i][j-1] and not ladder[i][j] and not ladder[i][j+1]:
                ladder[i][j] = 1
                dfs(i, laddercnt+1)
                if flag:
                    return
                ladder[i][j] = 0


for i in range(4):
    need = i
    dfs(1, 0)
    if flag:
        print(need)
        break

if not flag:
    print(-1)
