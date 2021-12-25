

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


n,m = map(int, input().split())
street = []
total = 0
for _ in range(m):
    data = list(map(int, input().split()))
    street.append(data)
    total += data[2]
street.sort(key=lambda x:x[2])
result = 0
parent = [i for i in range(n)]

for a,b,c in street:
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result += c
print(total-result)