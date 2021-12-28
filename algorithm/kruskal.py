from typing import List


# 특정 원소가 속한 집합을 찾기
# 경로 압축을 통해 호출할때마다 루트 노드 갱신이 가능하면 갱신
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):

    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def kruskal(v, e, edges: List[List[int]]):
    parent = [0] * (v + 1)
    result = 0

    # 부모 테이블 상에서 부모를 자기 자신으로 초기화
    for i in range(1, v + 1):
        parent[i] = i

    # 간선 비용을 기준으로 정렬
    edges.sort(key=lambda x: x[2])

    for u, v, w in edges:
        # 두 노드의 루트 노드가 서로 같지 않다면(같은 집합에 포함된 것이 아니라면)
        # 사이클이 아닌 것이며 집합에 포함
        if find_parent(parent, u) != find_parent(parent, v):
            union_parent(parent, u, v)
            result += w

    print(result)


kruskal(7, 9, [[1, 2, 29],[1, 5, 75],[2, 3, 35],[2, 6, 34],[3, 4, 7],[4, 6, 23],[4, 7, 13],[5, 6, 53],[6, 7, 25]])
