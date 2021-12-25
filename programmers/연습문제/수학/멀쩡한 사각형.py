import math
def solution(w,h):
    answer = 1
    return w*h - (w+h-math.gcd(w,h))

print(solution(3, 3))
print(solution(2, 1))
print(solution(2, 2))
print(solution(2, 3))
print(solution(2, 4))