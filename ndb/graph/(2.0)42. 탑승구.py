
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

def my_answer(g, p, data):

    parent = []
    for i in range(g+1):
        parent.append(i)

    result = 0

    for plain in data:
        root = find_parent(parent, plain)
        if root == 0:
            break
        else:
            union_parent(parent, root, root-1)
            result += 1

    print(result)

my_answer(4,3,[4,1,1])
my_answer(4,6,[2,2,3,3,4,4])