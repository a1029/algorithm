from typing import List
import collections


class Solution:

    def floyd_warshall_algorithm(self, n, m, times: List[List[int]]):

        inf = int(1e9)
        graph = [[inf] * (n + 1) for _ in range(n + 1)]
        # 자기자신으로 가는 거리는 0
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if i == j:
                    graph[i][j] = 0
        # 초기 입력값 설정
        for u, v, w in times:
            graph[u][v] = w

        # 플로이드 워셜 알고리즘 수행
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] == inf:
                    print("inf", end=' ')
                else:
                    print(graph[i][j], end=' ')
            print()


p = Solution()
p.floyd_warshall_algorithm(4, 7, [[1, 2, 4],
                                  [1, 4, 6],
                                  [2, 1, 3],
                                  [2, 3, 7],
                                  [3, 1, 5],
                                  [3, 4, 4],
                                  [4, 3, 2]])
