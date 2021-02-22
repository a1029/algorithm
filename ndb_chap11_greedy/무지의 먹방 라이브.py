from typing import List
import heapq


# self-solving : X
def solution(food_times: List[int], k):
    if sum(food_times) <= k:
        return -1

    heap = []
    for i, time in enumerate(food_times):
        heapq.heappush(heap, (time, i + 1))

    sum_value = 0
    previous = 0
    length = len(food_times)

    while sum_value + ((heap[0][0] - previous) * length) <= k:
        now = heapq.heappop(heap)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(heap, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]


print(solution([3, 1, 2], 5))  # 1
print(solution([2, 0, 3], 4))  # 3
print(solution([2, 2, 1], 7))  # -1
