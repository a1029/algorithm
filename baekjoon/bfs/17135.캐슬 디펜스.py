import itertools
import copy
import collections
def noe():
    for i in range(n):
        for j in range(m):
            if temp_arr[i][j] == 1:
                q.append((i,j))
def attack(q):
    global result
    target = [(0,1e9),(0,1e9),(0,1e9)]
    dist = [1e9,1e9,1e9]
    while q:
        x,y = q.popleft()
        for i in range(3):
            tmp = abs(n-x) + abs(case[i]-y)
            if dist[i] > tmp:
                dist[i] = tmp
                target[i] = (x,y)
            elif dist[i] == tmp and y < target[i][1]:
                target[i] = (x,y)
    for i,(x,y) in enumerate(target):
        if temp_arr[x][y] == 1:
            if dist[i] <= d:
                temp_arr[x][y] = 0
                result += 1

n,m,d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
archer = [i for i in range(m)]
answer = 0
q = collections.deque()
for case in itertools.combinations(archer, 3):
    temp_arr = copy.deepcopy(arr)
    result = 0
    while True:
        noe()
        if len(q)==0:
            break
        attack(q)
        temp_arr = [[0]*m] + temp_arr[:n-1]
    answer = max(answer, result)
print(answer)
