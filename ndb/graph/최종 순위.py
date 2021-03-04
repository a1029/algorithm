from collections import deque


# X
def my_answer(n, data, m, data2):
    indegree = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]].append(data[j])
            indegree[data[j]] += 1

    for a, b in data2:
        indegree[a] -= 1
        if indegree[a] < 0:
            print("IMPOSSIBLE")
            return
        indegree[b] += 1
        graph[a].append(b)
        graph[b].remove(a)


    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break
        now = q.popleft()
        result.append(now)
        for n in graph[now]:
            indegree[n] -= 1
            if indegree[n] == 0:
                q.append(n)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()


def solution(n, data, m, data2):
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for i in range(n + 1)]

    for i in range(n):
        for j in range(i + 1, n):
            graph[data[i]][data[j]] = True
            indegree[data[j]] += 1

    for a, b in data2:
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) >= 2:
            certain = False
            break
        now = q.popleft()
        result.append(now)
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in result:
            print(i, end=' ')
        print()


my_answer(5, [5, 4, 3, 2, 1], 2, [[2, 4], [3, 4]])
my_answer(3, [2, 3, 1], 0, [])
my_answer(4, [1, 2, 3, 4], 3, [[1, 2], [3, 4], [2, 3]])
solution(5, [5, 4, 3, 2, 1], 2, [[2, 4], [3, 4]])
solution(3, [2, 3, 1], 0, [])
solution(4, [1, 2, 3, 4], 3, [[1, 2], [3, 4], [2, 3]])
