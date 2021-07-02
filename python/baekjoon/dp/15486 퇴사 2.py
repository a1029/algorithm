import sys

n = int(sys.stdin.readline().rstrip())
t,p = [],[]
dp = [0]*(n+1)
max_value = 0
for i in range(n):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    t.append(a)
    p.append(b)

for i in range(n-1, -1, -1):
    time = t[i]+i
    if time<=n:
        dp[i] = max(max_value, p[i] + dp[t[i]+i])
        max_value = dp[i]
    else:
        dp[i] = max_value
print(max(dp))