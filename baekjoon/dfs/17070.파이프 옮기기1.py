import sys
def dfs(x,y,shape):
    global result
    if x==n-1 and y==n-1:
        result+=1
        return
    if shape==0 or shape==2:
        if y+1<n:
            if not arr[x][y+1]:
                dfs(x,y+1,0)
    if shape==1 or shape==2:
        if x+1<n:
            if not arr[x+1][y]:
                dfs(x+1,y,1)
    if shape==0 or shape==1 or shape==2:
        if x+1<n and y+1<n:
            if not arr[x][y+1] and not arr[x+1][y] and not arr[x+1][y+1]:
                dfs(x+1,y+1,2)

n = int(input())
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
result = 0
dfs(0,1,0)
print(result)