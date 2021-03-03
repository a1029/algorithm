import copy

# O
def my_answer(n, data):
    dp = copy.deepcopy(data)

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = data[i][j] + dp[i-1][j]
            elif j == i:
                dp[i][j] = data[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] = data[i][j] + max(dp[i-1][j-1], dp[i-1][j])

    result = max(dp[-1])
    print(result)


my_answer(5, [[7],
              [3, 8],
              [8, 1, 0],
              [2, 7, 4, 4],
              [4, 5, 2, 6, 5]])
