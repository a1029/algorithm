
n = int(input())
data = list(map(int, input().split()))
m = int(input())

dp = [[0]*(n+1) for _ in range(4)]

for i in range(1, n):
    data[i] = data[i-1] + data[i]
data.insert(0, 0)

for i in range(1, 4):
    for j in range(i*m, n+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-m] + (data[j]-data[j-m]))

print(dp[3][n])