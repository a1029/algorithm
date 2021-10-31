
n,s,m = map(int, input().split())
volume = list(map(int, input().split()))
dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1
for i in range(1,n+1):
    for j in range(m+1):
        if dp[i-1][j]==0:
            continue
        if j+volume[i-1]<=m:
            dp[i][j+volume[i-1]] = 1
        if j-volume[i-1]>=0:
            dp[i][j-volume[i-1]] = 1
result = -1
for i in range(m,-1,-1):
    if dp[n][i]:
        result = i
        break
print(result)
