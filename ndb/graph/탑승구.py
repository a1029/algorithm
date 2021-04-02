
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


g = int(input())
p = int(input())
parent = [i for i in range(g+1)]
count = 0
for _ in range(p):
    cur = find_parent(parent, int(input()))
    if cur==0:
        print(count)
        break
    else:
        union_parent(parent, cur, cur-1)
        count+=1