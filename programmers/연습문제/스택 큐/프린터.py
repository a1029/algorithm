from collections import deque
def solution(priorities, location):
    q = deque([[i, p] for i,p in enumerate(priorities)])
    answer = 1
    while q:
        i1,p1 = q.popleft()
        if any(p1 < p2 for i2,p2 in q):
            q.append([i1,p1])
        else:
            if i1==location:
                return answer
            else:
                answer += 1

def solution2(priorities, location):
    answer = 0
    r = sorted(priorities, reverse=True)
    r_idx = 0
    while True:
        for i,p in enumerate(priorities):
            if p==r[r_idx]:
                answer += 1
                r_idx += 1
                if i==location:
                    return answer
        
        
print(solution2([2,1,3,2], 2))
print(solution2([1,1,9,1,1,1], 0))