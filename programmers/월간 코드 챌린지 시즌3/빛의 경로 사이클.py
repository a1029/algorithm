def solution(grid):
    answer = []
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    dmap = { 'S': 0, 'R': 1, 'L': 2}
    dtrans = [[0,1,3],[1,2,0],[2,3,1],[3,0,2]]
    n = len(grid)
    m = len(grid[0])
    visit = [[[0]*4 for _ in range(m)] for _ in range(n)]
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            for i in range(4):
                if(visit[x][y][i]):
                    continue
                d = i
                nx = x
                ny = y
                count = 0
                while (not visit[nx][ny][d]):
                    count += 1
                    visit[nx][ny][d] = 1
                    d = dtrans[d][dmap[grid[nx][ny]]]
                    nx += dx[d]
                    ny += dy[d]
                    if nx>=n:
                        nx = 0
                    elif nx==-1:
                        nx = n-1
                    if ny>=m:
                        ny = 0
                    elif ny==-1:
                        ny = m-1
                answer.append(count)

    answer.sort()
    return answer

solution(["SL", "LR"])
solution(["S"])
solution(["R", "R"])