def solution(n, times):
    answer = 0
    l = 0
    r = times[-1] * n
    while l <= r:
        mid = (l + r) // 2
        s = sum(map(lambda x : mid // x, times))
        if s < n:
            l = mid + 1
        else:
            r = mid - 1
            answer = mid
    
    return answer

#print(solution(6,[7,10])) # 28
print(solution(10,[6,8,10])) # 30