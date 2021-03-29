import itertools

def dfs(i,j):
    if i<0 or i>=n or j<0 or j>=m or tmp[i][j]==1 or tmp[i][j]==3:
        return
    tmp[i][j] = 3

    dfs(i,j+1)
    dfs(i,j-1)
    dfs(i+1,j)
    dfs(i-1,j)

def check():
    count = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==0:
                count+=1
    return count

n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
empty = []
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            empty.append([i,j])
result = 0
for case in itertools.combinations(empty, 3):
    tmp = [arr[i][:] for i in range(n)]
    for x,y in case:
        tmp[x][y] = 1
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==2:
                dfs(i,j)
    result = max(result, check())
print(result)