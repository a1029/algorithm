def solution(n, s):
    if n>s:
        return [-1]
    a,b = divmod(s, n)
    answer = [a for i in range(n)]
    for i in range(b):
        answer[-i-1] += 1
    return answer

print(solution(3,8))