from collections import deque

# O(n^2)
def solution(progresses, speeds):
    answer = []
    q = deque(zip(progresses, speeds))
    while q:
        for _ in range(len(q)):
            p, s = q.popleft()
            if p < 100:
                p += s
            q.append([p,s])

        count = 0
        for _ in range(len(q)):
            if q[0][0] < 100:
                break
            p, s = q.popleft()
            count += 1
        if count > 0:
            answer.append(count)

    return answer

# O(n)
def solution2(progresses, speeds):
    answer = []
    q = deque(zip(progresses, speeds))
    time = 0
    count = 0
    while q:
        if q[0][0] + time * q[0][1] >= 100:
            q.popleft()
            count += 1
        else:
            if count != 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
            
