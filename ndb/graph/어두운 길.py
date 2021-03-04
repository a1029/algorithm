

# O
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


def my_answer(n, m, data):

    data.sort(key=lambda x: x[2])
    total = 0
    result = 0
    parent = [0]*n
    for i in range(n):
        parent[i] = i

    for x,y,cost in data:
        total += cost
        if find_parent(parent, x) != find_parent(parent, y):
            union_parent(parent, x, y)
            result += cost

    print(total-result)
    print(list(map(sum, zip(*data)))[2]-result)


my_answer(7, 11,
          [[0,1,7],
           [0,3,5],
           [1,2,8],
           [1,3,9],
           [1,4,7],
           [2,4,5],
           [3,4,15],
           [3,5,6],
           [4,5,8],
           [4,6,9],
           [5,6,11]])