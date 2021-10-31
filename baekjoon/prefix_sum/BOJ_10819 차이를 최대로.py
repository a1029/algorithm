import itertools

n = int(input())
data = list(map(int, input().split()))

result = 0
for case in itertools.permutations(data):

    tmp = 0
    for i in range(n-1):
        tmp += abs(case[i]-case[i+1])
    result = max(result, tmp)

print(result)

String = [0]*n
visited = [False]*n
result = 0
def dfs(index):

    global result

    if index == n:
        tmp = 0
        for i in range(n-1):
            tmp += abs(String[i]-String[i+1])
        result = max(result, tmp)
        return

    else:
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            String[index] = data[i]
            dfs(index+1)
            visited[i] = False

dfs(0)
print(result)
