import copy

# fail
def solution(n, m, data):
    dp = copy.deepcopy(data)

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            left = dp[i][j - 1]
            dp[i][j] = data[i][j] + max(left_up, left, left_down)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)


solution(3, 4, [[1, 3, 3, 2],
                 [2, 1, 4, 1],
                 [0, 6, 4, 7]])
solution(4, 4, [[1, 3, 1, 5],
                 [2, 2, 4, 1],
                 [5, 0, 2, 3],
                 [0, 6, 1, 2]])
