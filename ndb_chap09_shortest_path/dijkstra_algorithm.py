from typing import List
import heapq
import collections


class Solution:


    def dijkstra_algorithm(self, n, m, times: List[List[int]]):

        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        inf = int(1e9)
        distance = [inf] * (n + 1)
        start = 1

        # 최단 거리가 가장 짧은 노드를 선택하기 위한 최소힙 사용
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            # 최단 거리가 가장 짧은 노드 선택
            dist, node = heapq.heappop(q)
            # 선택한 노드가 이미 최단거리라면 건너뜀
            if distance[node] < dist:
                continue
            # 선택한 노드의 인접 노드 탐색
            for v, w in graph[node]:
                cost = dist + w
                # 선택한 노드를 거쳐서 인접 노드로 가는 거리가 더 짧은 경우
                if cost < distance[v]:
                    # 거리 갱신
                    distance[v] = cost
                    heapq.heappush(q, (cost, v))

        for i in range(1, n+1):
            if distance[i] == inf:
                print("inf", end=' ')
            else:
                print(distance[i], end=' ')


p = Solution()
p.dijkstra_algorithm(6, 11, [[1, 2, 2],
                             [1, 3, 5],
                             [1, 4, 1],
                             [2, 3, 3],
                             [2, 4, 2],
                             [3, 2, 3],
                             [3, 6, 5],
                             [4, 3, 3],
                             [4, 5, 1],
                             [5, 3, 1],
                             [5, 6, 2]])
