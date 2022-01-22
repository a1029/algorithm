import math
def solution(n, stations, w):
    answer = 0

    able = []
    if stations[0]-w > 1:
        able.append([1, stations[0]-w-1])

    for i in range(len(stations)-1):
        able.append([stations[i]+w+1, stations[i+1]-w-1])

    if stations[-1]+w < n:
        able.append([stations[-1]+w+1, n])
    
    for a,b in able:
        answer += math.ceil((b-a+1)/(w*2+1))

    return answer


def solution2(n, stations, w):
    answer = 0
    W = 2 * w + 1
    
    start = 1
    for s in stations:
        answer += max(math.ceil((s - w - start) / W), 0)
        start = s + w + 1
        
    if n >= start:
        answer += math.ceil((n - start + 1) / W)
    
    return answer

print(solution(11, [4,11], 1))
print(solution(16, [9], 2))