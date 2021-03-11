import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
data2 = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]
dp = [[0]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + data[i-1][j-1]


for a,b,c,d in data2:
    print(dp[c][d] - dp[a-1][d] - dp[c][b-1] + dp[a-1][b-1])

