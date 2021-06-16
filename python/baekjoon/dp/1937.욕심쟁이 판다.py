import sys
sys.setrecursionlimit(10**6)
n = int(input())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def dfs(x,y):

    if dp[x][y] == 0:
        dp[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and data[x][y] < data[nx][ny]:
                dp[x][y] = max(dp[x][y], dfs(nx,ny)+1)

    return dp[x][y]

result = 0
for x in range(n):
    for y in range(n):
        result = max(result, dfs(x,y))

print(result)