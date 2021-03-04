

# X O
def solution(n, data):

    data.reverse()
    dp = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if data[j] < data[i]:
                dp[i] = max(dp[i], dp[j]+1)

    print(dp)


solution(7, [15, 11, 4, 8, 5, 2, 4])
