def dfs(arr, x, n):
    if x==n:
        return 1
    count = 0

    for y in range(n):
        arr[x] = y
        for i in range(x):
            if arr[x] == arr[i] or abs(arr[x] - arr[i]) == x - i:
                break
        else:
            count += dfs(arr, x+1, n)
    return count

def solution(n):
    arr = [0]*n
    answer = dfs(arr, 0, n)
    return answer

print(solution(12))