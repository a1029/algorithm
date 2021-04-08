import sys
import heapq
n = int(input())
left,right = [],[]
for _ in range(n):
    num = int(sys.stdin.readline())
    if len(left)==len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))

    if right and left[0][1] > right[0][1]:
        l = heapq.heappop(left)[1]
        r = heapq.heappop(right)[1]
        heapq.heappush(right, (l, l))
        heapq.heappush(left, (-r, r))
    print(left[0][1])
