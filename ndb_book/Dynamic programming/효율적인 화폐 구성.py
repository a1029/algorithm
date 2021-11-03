
n,m = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [10001]*(m+1)
dp[0] = 0
for i in range(coin[0], m+1):
    for c in coin:
        dp[i] = min(dp[i], dp[i-c]+1)

print(dp[m] if dp[m] != 10001 else -1)