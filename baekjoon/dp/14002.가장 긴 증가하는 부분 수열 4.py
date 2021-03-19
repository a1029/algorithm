n = int(input())
data = list(map(int, input().split()))

dp = [1]*n
for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

a = max(dp)
b = dp.index(a)
result = [data[b]]
for i in range(b, -1, -1):
    if dp[i] == a-1:
        result.append(data[i])
        a = dp[i]

result.sort()
for i in result:
    print(i, end=" ")