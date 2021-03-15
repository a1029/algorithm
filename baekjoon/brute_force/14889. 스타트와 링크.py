import sys

def dfs(a, count):

    global result
    if count == n//2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if select[i] and select[j]:
                    start += data[i][j]
                elif not select[i] and not select[j]:
                    link += data[i][j]
        result = min(result, abs(start-link))

    for i in range(a, n):
        if select[i]:
            continue
        select[i] = 1
        dfs(i+1, count+1)
        select[i] = 0


n = int(input())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
select = [0 for _ in range(n)]
result = 1e9
dfs(0, 0)
print(result)
