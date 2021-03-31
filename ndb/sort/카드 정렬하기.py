import heapq
import sys
n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(sys.stdin.readline().rstrip()))

result = 0
while q:
    if len(q)>=2:
        a = heapq.heappop(q)
        b = heapq.heappop(q)
        result += a+b
        heapq.heappush(q, a+b)
    else:
        print(result)
        break