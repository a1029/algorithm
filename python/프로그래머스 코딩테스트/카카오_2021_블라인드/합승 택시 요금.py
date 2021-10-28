import collections
import heapq

def solution(n, s, a, b, fares):

    graph = collections.defaultdict(list)
    for v,w,e in fares:
        graph[v].append([w,e])
        graph[w].append([v,e])

    def get_dist(start_node):
        dist = [int(1e9)] * (n + 1)
        start = start_node
        dist[start] = 0
        q = [(dist[start], start)]
        while q:
            cost, now = heapq.heappop(q)
            if dist[now] < cost:
                continue
            for nxt, nxt_cost in graph[now]:
                sum_cost = nxt_cost + cost
                if sum_cost < dist[nxt]:
                    dist[nxt] = sum_cost
                    heapq.heappush(q, (dist[nxt], nxt))
        return dist

    answer = int(1e9)
    for i in range(1,n+1):
        dist = get_dist(i)
        answer = min(answer, dist[s]+dist[a]+dist[b])
    return answer

solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])