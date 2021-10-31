import collections
import sys
import heapq

n, m = map(int, input().split())
fox = [[] for _ in range(n+1)]
wolf = [[] for _ in range(n+1)]
dist_fox = [1e9]*(n+1)
dist_wolf_fast = [1e9]*(n+1)
dist_wolf_slow = [1e9]*(n+1)

dist_fox[1] = 0
dist_wolf_fast[1] = 0
dist_wolf_slow[1] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    fox[a].append([b, c*2])
    fox[b].append([a, c*2])
    wolf[a].append([b, c, c*2*2])
    wolf[b].append([a, c, c*2*2])

q = []
heapq.heappush(q, (0, 1))
while q:
    now_cost, now = heapq.heappop(q)
    for nxt, nxt_cost in fox[now]:
        cost = now_cost + nxt_cost
        if cost < dist_fox[nxt]:
            dist_fox[nxt] = cost
            heapq.heappush(q, (cost, nxt))

q = []
heapq.heappush(q, (0, 1, "fast"))
while q:
    cost, now, state = heapq.heappop(q)
    if state == "fast":
        if dist_wolf_slow[now] != cost:
            continue
    else:
        if dist_wolf_fast[now] != cost:
            continue
    for nxt, nxt_half, nxt_double in wolf[now]:
        if state == "fast":
            cost = dist_wolf_slow[now] + nxt_half
            if cost < dist_wolf_fast[nxt]:
                dist_wolf_fast[nxt] = cost
                heapq.heappush(q, (cost, nxt, "slow"))
        else:
            cost = dist_wolf_fast[now] + nxt_double
            if cost < dist_wolf_slow[nxt]:
                dist_wolf_slow[nxt] = cost
                heapq.heappush(q, (cost, nxt, "fast"))

result = 0
for i in range(1, n+1):
    if dist_fox[i] < min(dist_wolf_fast[i], dist_wolf_slow[i]):
        result += 1

print(result)
