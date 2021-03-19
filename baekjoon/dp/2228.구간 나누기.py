import sys

def dfs(n, m):
    if m == 0:
        return 0
    if n < 0:
        return -sys.maxsize
    if dp[n][m]:
        return dp[n][m]

    dp[n][m] = dfs(n-1, m)
    for i in range(n, -1, -1):
        dp[n][m] = max(dp[n][m], dfs(i-2, m-1) + (prefix_sum[n] - prefix_sum[i-1]))

    return dp[n][m]


n, m = map(int, input().split())
prefix_sum = [0]*(n+1)
for i in range(1, n+1):
    num = int(input())
    prefix_sum[i] = prefix_sum[i-1] + num
dp = [[0]*(m+1) for _ in range(n+1)]

print(dfs(n,m))