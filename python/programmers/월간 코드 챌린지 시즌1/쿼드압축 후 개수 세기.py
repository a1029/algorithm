
answer = [0,0]
def divide(arr,i,j,n):
    seed = arr[i][j]
    c = True
    for x in range(i,i+n):
        for y in range(j,j+n):
            if arr[x][y]!=seed:
                c = False
    if c:
        answer[seed]+=1
    else:
        n = n//2
        divide(arr,i,j,n)
        divide(arr,i,j+n,n)
        divide(arr,i+n,j,n)
        divide(arr,i+n,j+n,n)

def solution(arr):
    divide(arr,0,0,len(arr))
    return answer