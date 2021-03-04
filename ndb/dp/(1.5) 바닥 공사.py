
# X
def my_answer(n):

    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + 2*dp[i-2]) % 796796

    print(dp[n])


my_answer(3)