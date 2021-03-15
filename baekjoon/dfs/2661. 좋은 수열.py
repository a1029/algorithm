import sys

def dfs(s, c):
    for i in range(1, c//2+1):
        if s[-i:] == s[-2*i:-i]:
            return
    if c == n:
        print(s)
        sys.exit()

    for i in ['1', '2', '3']:
        dfs(s+i, c+1)

n = int(input())
dfs('1', 1)
