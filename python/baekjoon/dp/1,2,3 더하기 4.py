
a = []
for i in range(int(input())):
    a.append(int(input()))
dp = [1]*10001
for i in range(2, 10001):
    dp[i] += dp[i-2]
for i in range(3, 10001):
    dp[i] += dp[i-3]
for x in a:
    print(dp[x])