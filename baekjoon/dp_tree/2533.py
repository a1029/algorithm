import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
dp = [[0, 0] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(prev, u):
    dp[u][0] = 0
    dp[u][1] = 1
    for v in tree[u]:
        if prev != v:
            dfs(u, v)
            dp[u][0] += dp[v][1]
            dp[u][1] += min(dp[v][0], dp[v][1])

dfs(0, 1)
print(min(dp[1][0], dp[1][1]))