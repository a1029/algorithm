
# O
n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input())))

result = []
count = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(i, j):

    global count
    if i < 0 or i >= n or j < 0 or j >= n or data[i][j] == 0:
        return

    data[i][j] = 0
    count += 1
    dfs(i, j + 1)
    dfs(i, j - 1)
    dfs(i + 1, j)
    dfs(i - 1, j)

    return count


for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            count = 0
            result.append(dfs(i, j))

result.sort()
print(len(result))
for n in result:
    print(n)
