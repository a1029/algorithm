import collections
from typing import List


def topology_sort(v, e, array: List[List[int]]):

    # 모든 노드의 진입차수를 0으로 초기화
    indegree = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]
    for a, b in array:
        graph[a].append(b)
        indegree[b] += 1

    print(graph)
    result = []
    q = collections.deque()

    for i in range(1, v + 1):
        # 처음 시작노드는 진입차수가 0이므로 삽입
        if indegree[i] == 0:
            q.append(i)

    while q:
        # 진입차수가 0인 노드를 큐에서 추출
        node = q.popleft()
        result.append(node)
        # 해당 노드와 연결된 인접노드들에 대하여
        for i in graph[node]:
            # 인접노드 연결 끊기(진입차수 -1)
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    print(result)


topology_sort(7, 8, [[1, 2],
                     [1, 5],
                     [2, 3],
                     [2, 6],
                     [3, 4],
                     [4, 7],
                     [5, 6],
                     [6, 4]])
