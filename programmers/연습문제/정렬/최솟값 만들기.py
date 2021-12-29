def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    answer = sum(map(lambda x: x[0]*x[1], list(zip(*[A,B]))))

    return answer

print(solution([1,4,2],[5,4,4]))