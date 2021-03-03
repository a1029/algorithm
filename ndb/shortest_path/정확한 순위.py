
# O
def my_answer(n, m, data):

    graph = [[1e9]*(n+1) for _ in range(n+1)]

    for i, j in data:
        graph[i][j] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    for i in range(n+1):
        for j in range(n+1):
            if graph[i][j] == 1e9:
                graph[i][j] = 0

    result = 0

    for i in range(1, n+1):
        count = 0
        for j in range(1, n+1):
            if graph[i][j]+graph[j][i] >= 1:
                count += 1
        if count == n-1:
            result += 1

    print(result)


my_answer(6, 6,
          [[1, 5],
           [3, 4],
           [4, 2],
           [4, 6],
           [5, 2],
           [5, 4]])
