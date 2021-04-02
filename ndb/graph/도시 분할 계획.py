import sys
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

n,m = map(int,input().split())
parent = [i for i in range(n+1)]
paths = []
result = 0
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    paths.append((c,a,b))
paths.sort()

last = 0
for c,a,b in paths:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent,a,b)
        result += c
        last = c
result -= last
print(result)