# https://programmers.co.kr/learn/courses/30/lessons/12985
def solution(n,a,b):
    answer = 0
    if a>b:
        a,b = b,a
    while True:
        if a%2==1 and b%2==0 and abs(a-b)<=1:
            break
        if a%2==1: a += 1
        if b%2==1: b += 1
        a /= 2
        b /= 2
        answer += 1
    return answer + 1
    
print(solution(8,4,7)) # 3
print(solution(8,4,5)) # 3
print(solution(8,6,7)) # 2