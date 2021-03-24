import heapq
import collections


def my_answer(n, m, k, x, data):
    graph = collections.defaultdict(list)
    for u, v in data:
        graph[u].append(v)

    dist = [1e9] * (n + 1)
    prev = [0] * (n + 1)
    start = x
    dist[start] = 0
    prev[start] = start
    q = []
    for v in range(n):
        heapq.heappush(q, (dist[v], v))

    while q:
        d, node = heapq.heappop(q)
        for neighbor in graph[node]:
            cost = dist[node] + 1
            if cost < dist[neighbor]:
                dist[neighbor] = cost
                prev[neighbor] = node

    result = [i for i in range(1, len(dist)) if dist[i] == k]
    print(result) if len(result) != 0 else print(-1)


def solution(n, m, k, x, data):
    graph = collections.defaultdict(list)
    for u, v in data:
        graph[u].append(v)
    dist = [-1] * (n + 1)
    dist[x] = 0
    q = collections.deque([x])
    while q:
        node = q.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)

    result = [i for i in range(1, len(dist)) if dist[i] == k]
    print(result) if len(result) != 0 else print(-1)


my_answer(4, 4, 2, 1,  # 4
          [[1, 2],
           [1, 3],
           [2, 3],
           [2, 4]])
my_answer(4, 3, 2, 1,  # -1
          [[1, 2],
           [1, 3],
           [1, 4]])
my_answer(4, 4, 1, 1,  # 2 3
          [[1, 2],
           [1, 3],
           [2, 3],
           [2, 4]])
solution(4, 4, 2, 1,  # 4
         [[1, 2],
          [1, 3],
          [2, 3],
          [2, 4]])
solution(4, 3, 2, 1,  # -1
         [[1, 2],
          [1, 3],
          [1, 4]])
solution(4, 4, 1, 1,  # 2 3
         [[1, 2],
          [1, 3],
          [2, 3],
          [2, 4]])
