from collections import defaultdict
import heapq
import sys
n, m = map(int, input().split())
start = int(input())
data = defaultdict(list)
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    data[a].append([b,c])
dist = [1e9]*(n+1)

dist[start] = 0
q = []
heapq.heappush(q, (dist[start], start))
while q:
    e,v = heapq.heappop(q)
    for w,c in data[v]:
        cost = e + c
        if dist[w] > cost:
            dist[w] = cost
            heapq.heappush(q, (cost, w))

for i in range(1, len(dist)):
    if dist[i]==1e9:
        print("INF")
    else:
        print(dist[i])