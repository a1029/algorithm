import sys

n, m = map(int, input().split())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
right = [0]*m
left = [0]*m


dp[0][0] = data[0][0]
for j in range(1, m):
    dp[0][j] = dp[0][j-1] + data[0][j]


for i in range(1, n):
    right[0] = dp[i-1][0] + data[i][0]
    for j in range(1, m):
        right[j] = max(right[j-1], dp[i-1][j]) + data[i][j]

    left[m-1] = dp[i-1][m-1] + data[i][m-1]
    for j in range(m-2, -1, -1):
        left[j] = max(left[j+1], dp[i-1][j]) + data[i][j]

    for k in range(m):
        dp[i][k] = max(right[k], left[k])

print(dp[n-1][m-1])
