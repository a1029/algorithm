import sys
n = int(input())
arr = list(map(int, input().split()))
add,sub,mul,div = map(int, input().split())
min_value, max_value = sys.maxsize, -sys.maxsize

def dfs(prev, index):
    global max_value,min_value,add,sub,mul,div
    if index==len(arr):
        max_value = max(max_value, prev)
        min_value = min(min_value, prev)
        return
    if add>0:
        add-=1
        dfs(prev+arr[index], index+1)
        add+=1
    if sub>0:
        sub-=1
        dfs(prev-arr[index], index+1)
        sub+=1
    if mul>0:
        mul-=1
        dfs(prev*arr[index], index+1)
        mul+=1
    if div>0:
        div-=1
        dfs(int(prev/arr[index]), index+1)
        div+=1

dfs(arr[0],1)
print(max_value)
print(min_value)