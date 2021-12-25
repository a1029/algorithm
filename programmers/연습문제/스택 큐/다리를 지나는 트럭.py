from collections import deque

# https://programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    q = deque()
    while True:
        if q and answer-q[0][1]==bridge_length:
            q.popleft()
        if truck_weights and len(q)<bridge_length and truck_weights[0] + sum([w for w,_ in q]) <= weight:
            q.append([truck_weights.popleft(), answer])
        answer += 1
        if not q:
            break
    return answer

print(solution(2,10,[7, 4, 5, 6]))
print(solution(100,100,[10]))
print(solution(100,100,[10,10,10,10,10,10,10,10,10,10]))