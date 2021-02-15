from typing import List
import collections
import heapq


class Solution:

    # 자가풀이여부: O
    def my_answer(self, n, m, c, times: List[List[int]]):

        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        inf = int(1e9)
        start = c
        distance = [inf] * (n + 1)
        distance[start] = 0
        q = []
        heapq.heappush(q, (0, start))

        while q:
            dist, node = heapq.heappop(q)
            for u, v in graph[node]:
                cost = dist + v
                if cost < distance[u]:
                    distance[u] = cost
                    heapq.heappush(q, (cost, u))

        time = 0
        count = 0
        for t in distance:
            if t != inf:
                count +=1
                time = max(time, t)
        print(count-1, time)


p = Solution()
p.my_answer(3, 2, 1, [[1, 2, 4],
                      [1, 3, 2]])
