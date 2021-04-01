
for _ in range(int(input())):
    n,m = map(int, input().split())
    dp = []
    data = list(map(int, input().split()))
    for i in range(0, m*n, m):
        dp.append(data[i:i+m])
    for j in range(1,m):
        for i in range(n):
            if i==0:
                dp[i][j] += max(dp[i][j-1], dp[i+1][j-1])
            elif i==n-1:
                dp[i][j] += max(dp[i-1][j-1], dp[i][j-1])
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)
