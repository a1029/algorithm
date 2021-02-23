from typing import List
import heapq
import collections


class Solution:

    # success
    def my_answer(self, n, m, times: List[List[int]], x, k):

        inf = int(1e9)
        graph = [[inf] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if i == j:
                    graph[i][j] = 0

        for i, j in times:
            graph[i][j] = 1
            graph[j][i] = 1

        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

        result = graph[1][k]+graph[k][x]
        if result >= inf:
            print(-1)
        else:
            print(result)


p = Solution()
p.my_answer(5, 7, [[1, 2],
                   [1, 3],
                   [1, 4],
                   [2, 4],
                   [3, 4],
                   [3, 5],
                   [4, 5],
                   [4, 5]], 4, 5)
p.my_answer(4, 2, [[1, 3],
                   [2, 4]], 3, 4)
