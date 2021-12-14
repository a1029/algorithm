def solution(n):
    if n <= 3:
        return '124'[n-1]
    n, r = divmod(n-1, 3)
    return solution(n) + '124'[r]

print(solution(9))