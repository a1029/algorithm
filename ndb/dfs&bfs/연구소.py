import itertools
import copy


# success
def search(n, m, data):
    def dfs(i, j):

        if i < 0 or i >= len(data) or j < 0 or j >= len(data[0]) or data[i][j] == 1 or data[i][j] == 3:
            return
        data[i][j] = 3

        dfs(i, j + 1)
        dfs(i, j - 1, )
        dfs(i + 1, j)
        dfs(i - 1, j)

    for i in range(n):
        for j in range(m):
            if data[i][j] == 2:
                dfs(i, j)

    data = list(itertools.chain.from_iterable(data))
    result = data.count(0)
    return result


def my_answer(n, m, data):
    result = []
    sub_array = []
    temp = copy.deepcopy(data)
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                sub_array.append([i, j])
    for c in list(itertools.combinations(sub_array, 3)):
        for i, j in c:
            temp[i][j] = 1
        result.append(search(n, m, temp))
        temp = copy.deepcopy(data)

    print(max(result))


my_answer(7, 7, # 27
          [[2, 0, 0, 0, 1, 1, 0],
           [0, 0, 1, 0, 1, 2, 0],
           [0, 1, 1, 0, 1, 0, 0],
           [0, 1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 1],
           [0, 1, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0]])
my_answer(4, 6, # 9
          [[0, 0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0, 2],
           [1, 1, 1, 0, 0, 2],
           [0, 0, 0, 0, 0, 2]])
my_answer(8, 8, # 3
          [[2, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 0, 0, 0, 0, 0, 2],
           [2, 0, 0, 0, 0, 0, 0, 2],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0]])
