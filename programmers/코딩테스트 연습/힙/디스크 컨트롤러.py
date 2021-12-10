import heapq

def solution2(jobs):
    answer = 0
    curr_time = 0
    length = len(jobs)
    jobs.sort(key=lambda x: (x[1]))
    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= curr_time:
                curr_time += jobs[i][1]
                answer += curr_time - jobs[i][0]
                jobs.pop(i)
                break
            if i == len(jobs) - 1:
                curr_time += 1
    return int(answer / length)

def solution(jobs):
    answer = 0
    count = 0
    start = -1
    curr_time = 0
    heap = []
    while count != len(jobs):
        for i in range(len(jobs)):
            if start < jobs[i][0] <= curr_time:
                heapq.heappush(heap, (jobs[i][1], jobs[i][0]))
        if heap:
            a,b = heapq.heappop(heap)
            start = curr_time
            curr_time += a
            answer += curr_time - b
            count += 1
        else:
            curr_time += 1
    return int(answer / len(jobs))

print(solution([[0, 3], [1, 9], [2, 6]]))