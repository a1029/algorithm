import heapq

def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    q = []
    for i,time in enumerate(food_times):
        heapq.heappush(q, (time, i+1))

    ate_time = 0
    prev = 0
    length = len(food_times)
    while ate_time + (q[0][0]-prev)*length <= k:
        now = heapq.heappop(q)[0]
        ate_time += (now-prev) * length
        prev = now
        length -= 1

    q.sort(key=lambda x:x[1])
    return q[(k-ate_time)%length][1]