from collections import deque
import math
def solution(arr):
    answer = 0
    a,b = 6,8
    q = deque(arr)
    while len(q)>=2:
        a = q.popleft()
        b = q.popleft()
        r = a * b // math.gcd(a,b)
        q.append(r)
    return q[0]

solution([2,6,8,14])