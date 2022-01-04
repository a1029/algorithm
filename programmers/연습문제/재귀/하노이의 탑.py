def hanoi(answer, n, start, mid, end):
    if n == 1:
        answer.append([start, end])
        return
    hanoi(answer, n-1, start, end, mid)
    answer.append([start, end])
    hanoi(answer, n-1, mid, start, end)
    
    

def solution(n):
    answer = []
    hanoi(answer, n, 1, 2, 3)
    return answer

print(solution(20))