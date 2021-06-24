import sys

n, m = map(int, input().split())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + data[i-1][j-1]

print(dp[n][m])

dp = [[0]*(m+1) for _ in range(n+1)]
dp[1][1] = data[0][0]
for i in range(1, n+1):
    for j in range(1, m+1):
        if i==n and j==m:
            continue
        else:
            if i==n:
                dp[i][j+1] = max(dp[i][j+1], dp[i][j]+data[i-1][j])
            elif j==m:
                dp[i+1][j] = max(dp[i+1][j], dp[i][j]+data[i][j-1])
            else:
                dp[i][j+1] = max(dp[i][j+1], dp[i][j]+data[i-1][j])
                dp[i+1][j] = max(dp[i+1][j], dp[i][j] + data[i][j-1])
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + data[i][j])

print(dp[n][m])