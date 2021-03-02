

def my_answer(n, m, data):

    graph = [[1e9]*(n+1) for _ in range(n+1)]
    for i,j,cost in data:
        graph[i][j] = min(graph[i][j], cost)

    for i in range(n+1):
        graph[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == int(1e9):
                print(0, end=" ")
            else:
                print(graph[i][j], end=' ')
        print()

my_answer(5, 14, [[1,2,2],
                  [1,3,3],
                  [1,4,1],
                  [1,5,10],
                  [2,4,2],
                  [3,4,1],
                  [3,5,1],
                  [4,5,3],
                  [3,5,10],
                  [3,1,8],
                  [1,4,2],
                  [5,1,7],
                  [3,4,2],
                  [5,2,4]])