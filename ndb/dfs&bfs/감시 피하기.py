import itertools
import copy

# O
def my_answer(n, data):

    walls = []
    teachers = []
    count = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                walls.append([i, j])
            elif data[i][j] == 'T':
                teachers.append([i, j])

    def dfs(x, y, d):
        if x < 0 or x >= n or y < 0 or y >= n or data[x][y] == 'O' or data[x][y] == 'T':
            return True
        elif data[x][y] == 'S':
            return False
        if d == 0:
            return dfs(x, y + 1, 0)
        elif d == 1:
            return dfs(x + 1, y, 1)
        elif d == 2:
            return dfs(x, y - 1, 2)
        else:
            return dfs(x - 1, y, 3)

    for wall in list(itertools.combinations(walls, 3)):
        for i, j in wall:
            data[i][j] = 'O'
        for i, j in teachers:
            if dfs(i, j + 1, 0) and dfs(i + 1, j, 1) and dfs(i, j - 1, 2) and dfs(i - 1, j, 3):
                count += 1
        if count == len(teachers):
            print("YES")
            return
        count = 0
        for i, j in wall:
            data[i][j] = 'X'

    print("NO")
    return


def solution(n, data):
    walls = []
    teachers = []
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'X':
                walls.append([i, j])
            elif data[i][j] == 'T':
                teachers.append([i, j])

    def watch(x, y, direction):
        if direction == 0:
            while y >= 0:
                if data[x][y] == 'S':
                    return True
                if data[x][y] == 'O':
                    return False
                y -= 1
        if direction == 1:
            while y < n:
                if data[x][y] == 'S':
                    return True
                if data[x][y] == 'O':
                    return False
                y += 1
        if direction == 2:
            while x >= 0:
                if data[x][y] == 'S':
                    return True
                if data[x][y] == 'O':
                    return False
                x -= 1
        if direction == 3:
            while x < 0:
                if data[x][y] == 'S':
                    return True
                if data[x][y] == 'O':
                    return False
                x += 1
        return False

    def process():
        for x, y in teachers:
            for i in range(4):
                if watch(x, y, i):
                    return True
        return False

    for wall in itertools.combinations(walls, 3):
        for x, y in wall:
            data[x][y] = 'O'
        if not process():
            print("YES")
            return
        for x, y in wall:
            data[x][y] = 'X'
    print("NO")
    return


my_answer(5,    # NO
          [['X', 'S', 'X', 'X', 'T'],
           ['T', 'X', 'S', 'X', 'X'],
           ['X', 'X', 'X', 'X', 'X'],
           ['X', 'T', 'X', 'X', 'X'],
           ['X', 'X', 'T', 'X', 'X']])
my_answer(4,    # YES
          [['S', 'S', 'S', 'T'],
           ['X', 'X', 'X', 'X'],
           ['X', 'X', 'X', 'X'],
           ['T', 'T', 'T', 'X']])

solution(5,
          [['X', 'S', 'X', 'X', 'T'],
           ['T', 'X', 'S', 'X', 'X'],
           ['X', 'X', 'X', 'X', 'X'],
           ['X', 'T', 'X', 'X', 'X'],
           ['X', 'X', 'T', 'X', 'X']])
solution(4,
          [['S', 'S', 'S', 'T'],
           ['X', 'X', 'X', 'X'],
           ['X', 'X', 'X', 'X'],
           ['T', 'T', 'T', 'X']])
