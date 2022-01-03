def dfs(arr, row, n):
    if row==n:
        return 1
    
    count = 0
    for j in range(n):
        arr[row] = j
        for i in range(row):
            if arr[row] == arr[i] or abs(arr[row] - arr[i]) == row - i:
                break
        else:
            count += dfs(arr, row+1, n)
    return count
            
def solution(n):
    answer = 0
    arr = [0]*n
    answer = dfs(arr, 0, n)
    return answer

print(solution(4))