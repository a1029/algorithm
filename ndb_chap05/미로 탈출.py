from typing import List
import collections

class Solution:

    # 자가풀이여부: X
    def solution(self, n, m, input: List[str]):

        graph = [list(line) for line in input]
        graph = [list(map(int, line)) for line in graph]

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def bfs(x, y):
            dq = collections.deque()
            dq.append((x, y))
            while dq:
                x, y = dq.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= n or ny >= m or graph[nx][ny] == 0:
                        continue
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = graph[x][y] + 1
                        dq.append((nx, ny))

            return graph[n - 1][m - 1]

        print(bfs(0, 0))


p = Solution()

p.solution(5, 6, ['101010',
                   '111111',
                   '000001',
                   '111111',
                   '111111'])
