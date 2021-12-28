def solution(n):
    answer = 0
    for i in range(1,n//2+1):
        s = 0
        j = i
        while s <= n:
            if s == n:
                answer += 1
            s += j
            j += 1
    return answer + 1

def solution2(n):
    answer = 0
    return len([i for i in range(1, n+1, 2) if n%i==0])

print(solution(15))
