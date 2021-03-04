
# X O
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def cal_dist(a, b):
    x1,y1,z1 = a
    x2,y2,z2 = b
    return min(abs(x1-x2), abs(y1-y2), abs(z1-z2))


def my_answer(n, data):
    result = 0
    parent = [0] * n
    for i in range(n):
        parent[i] = i

    graph = []
    for i in range(n):
        for j in range(i+1, n):
            graph.append([i,j,cal_dist(data[i],data[j])])

    graph.sort(key=lambda x: x[2])
    for a,b,cost in graph:
        if find_parent(parent, a)!=find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(result)


def solution(n, data):

    parent = [0] * (n+1)
    for i in range(n+1):
        parent[i] = i

    graph = []
    x = []
    y = []
    z = []
    for i, data in enumerate(data):
        a, b, c = data
        x.append([a, i+1])
        y.append([b, i+1])
        z.append([c, i+1])

    x.sort()
    y.sort()
    z.sort()

    for i in range(n-1):
        graph.append([abs(x[i][0]-x[i+1][0]), x[i][1], x[i+1][1]])
        graph.append([abs(y[i][0]-y[i+1][0]), y[i][1], y[i+1][1]])
        graph.append([abs(z[i][0]-z[i+1][0]), z[i][1], z[i+1][1]])

    graph.sort()

    result = 0
    for cost, a, b in graph:
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(result)

solution(5,
          [[11, -15, -15],
           [14, -5, -15],
           [-1, -1, -5],
           [10, -4, -1],
           [19, -4, 19]])
