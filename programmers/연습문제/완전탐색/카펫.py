def solution(brown, yellow):
    answer = []
    for w in range(brown//2-1, -1, -1):
        h = 2 + (brown - 2*w) // 2
        if (w-2) * (h-2) == yellow:
            return [w,h]
    return answer

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))