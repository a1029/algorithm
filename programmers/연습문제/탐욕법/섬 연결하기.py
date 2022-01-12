def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]
    
def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a  

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    
    costs.sort(key=lambda x: x[2])

    for a,b,c in costs:
        if find_parent(a, parent) != find_parent(b, parent):
            union_parent(a, b, parent)
            answer += c

    return answer