import math
def solution(n, k):
    arr = [i+1 for i in range(n)]
    answer = []
    k = k-1
    while arr:
        idx = k // math.factorial(n-1)
        answer.append(arr[idx])
        arr.pop(idx)
        k = k % math.factorial(n-1)
        n -= 1
    return answer

print(solution(4,5))