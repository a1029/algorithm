def solution(m, n, puddles):
    answer = 0
    dp = [[0]*m for _ in range(n)]
    for j,i in puddles:
        dp[i-1][j-1] = -1
    for i in range(n):
        if dp[i][0]==-1:
            break
        dp[i][0] = 1
    for j in range(m):
        if dp[0][j]==-1:
            break
        dp[0][j] = 1
        
    for i in range(1, n):
        for j in range(1, m):
            if dp[i][j] == -1:
                continue
            if dp[i][j-1] != -1 and dp[i-1][j] != -1:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
            elif dp[i][j-1] != -1:
                dp[i][j] = dp[i][j-1]
            elif dp[i-1][j] != -1:
                dp[i][j] = dp[i-1][j]
    
    return dp[n-1][m-1]%1000000007

print(solution(4,3,[[1,2],[2,1]]))