import copy

# success
def my_answer(n, data):
    dp = copy.deepcopy(data)
    for i in range(n):
        m = 0
        for j in range(i - 1, -1, -1):
            if dp[j][0] <= i - j:
                m = max(m, dp[j][1])
        dp[i][1] = data[i][1] + m

    result = 0
    for i in range(n):
        if dp[i][0] <= n - i:
            result = max(result, dp[i][1])

    print(result)


def solution(n, data):
    t = []
    p = []
    dp = [0] * (n + 1)
    max_value = 0

    for d in data:
        t.append(d[0])
        p.append(d[1])

    for i in range(n - 1, -1, -1):
        time = t[i] + i
        if time <= n:
            dp[i] = max(p[i] + dp[time], max_value)
            max_value = dp[i]
        else:
            dp[i] = max_value

    print(max_value)


my_answer(7, [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]])
my_answer(10, [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]])
my_answer(10, [[5, 10], [5, 9], [5, 8], [5, 7], [5, 6], [5, 10], [5, 9], [5, 8], [5, 7], [5, 6]])
my_answer(10, [[5, 50], [4, 40], [3, 30], [2, 20], [1, 10], [1, 10], [2, 20], [3, 30], [4, 40], [5, 50]])
solution(7, [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]])
solution(10, [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9], [1, 10]])
solution(10, [[5, 10], [5, 9], [5, 8], [5, 7], [5, 6], [5, 10], [5, 9], [5, 8], [5, 7], [5, 6]])
solution(10, [[5, 50], [4, 40], [3, 30], [2, 20], [1, 10], [1, 10], [2, 20], [3, 30], [4, 40], [5, 50]])
