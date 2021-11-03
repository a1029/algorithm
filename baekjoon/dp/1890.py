
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1:
            break
        value = arr[i][j]
        nx = i + value
        ny = j + value
        if nx<n:
            dp[nx][j] += dp[i][j]
        if ny<n:
            dp[i][ny] += dp[i][j]
print(dp[n-1][n-1])