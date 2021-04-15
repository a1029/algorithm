
def solution(n):
    max_value = sum(x for x in range(n+1))
    arr = [[0]*n for _ in range(n)]

    i=j=0
    k = 1
    arr[i][j] = k
    while k<max_value:
        while i+1<n and arr[i+1][j]==0:
            i+=1
            k+=1
            arr[i][j] = k
        while j+1<n and arr[i][j+1]==0:
            j+=1
            k+=1
            arr[i][j] = k
        while i-1>0 and j-1>0 and arr[i-1][j-1]==0:
            i-=1
            j-=1
            k+=1
            arr[i][j] = k
    answer = []
    for i in range(n):
        for j in range(i+1):
            answer.append(arr[i][j])
    return answer
