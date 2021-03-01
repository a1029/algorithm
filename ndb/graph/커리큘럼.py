from typing import List
import collections
import copy

# fail
def my_answer(n, array: List[List[int]]):
    indegree = [0] * (n+1)
    graph = [[] for _ in range(n + 1)]
    time = [0] * (n+1)

    for i, a in enumerate(array):
        # 각 강의 시간 저장
        time[i+1] = a[0]

        for j in range(1, len(a)-1):
            # 선수강의 저장
            graph[a[j]].append(i+1)
        # 진입차수 저장
        indegree[i + 1] += len(a) - 2

    result = copy.deepcopy(time)
    q = collections.deque()

    for i in range(1, n + 1):
        # 시작강의는 선수강의가 0개
        if indegree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        # 현재 강의를 선수강의로 하는 다음 강의들에 대해서
        for i in graph[node]:
            # 전체시간 = 선수강의시간을 포함한 시간
            # 다음 강의 전체시간과 현재 강의 전체시간+다음 강의시간의 합 중 큰 값으로 저장
            result[i] = max(result[i], result[node]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    print([result[i] for i in range(1, len(result))])


my_answer(5, [[10, -1],
              [10, 1, -1],
              [4, 1, -1],
              [4, 3, 1, -1],
              [3, 3, -1]])
