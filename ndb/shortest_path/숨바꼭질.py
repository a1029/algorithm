import heapq

# success
def my_answer(n, m, data):
    graph = [[] for _ in range(n + 1)]
    for i, j in data:
        graph[i].append(j)
        graph[j].append(i)

    inf = int(1e9)
    distance = [inf] * (n + 1)
    start = 1
    distance[start] = 0
    q = [start]

    while q:
        node = heapq.heappop(q)
        for neighbor in graph[node]:
            cost = distance[node] + 1
            if cost < distance[neighbor]:
                distance[neighbor] = cost
                heapq.heappush(q, neighbor)

    a, b, c = [], 0, 0
    b = max(distance[1:])
    for i in range(1, n + 1):
        if distance[i] == b:
            a.append(i)

    print(min(a), b, len(a))


my_answer(6, 7,
          [[3, 6],
           [4, 3],
           [3, 2],
           [1, 3],
           [1, 2],
           [2, 4],
           [5, 2]])
