
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


def my_answer(n, m, data, data2):
    parent = [0] * (n+1)
    for i in range(n+1):
        parent[i] = i

    for i in range(n):
        for j in range(n):
            if data[i][j] == data[j][i] == 1:
                union_parent(parent, i+1, j+1)

    for i in range(len(data2)-1):
        if parent[data2[i]] != parent[data2[i+1]]:
            print("NO")
            return
    print("YES")


my_answer(5, 4,
          [[0, 1, 0, 1, 1],
           [1, 0, 1, 1, 0],
           [0, 1, 0, 0, 0],
           [1, 1, 0, 0, 0],
           [1, 0, 0, 0, 0]],
          [2, 3, 4, 3])
