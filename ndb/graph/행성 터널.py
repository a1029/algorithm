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

n = int(input())
x,y,z = [],[],[]
path = []
parent = [i for i in range(n+1)]
for i in range(1, n+1):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    x.append([a,i])
    y.append([b,i])
    z.append([c,i])
x.sort()
y.sort()
z.sort()
path = []
for i in range(n-1):
    path.append([x[i+1][0]-x[i][0], x[i+1][1], x[i][1]])
    path.append([y[i+1][0]-y[i][0], y[i+1][1], y[i][1]])
    path.append([z[i+1][0]-z[i][0], z[i+1][1], z[i][1]])
path.sort()

result = 0
for c,a,b in path:
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result += c
print(result)