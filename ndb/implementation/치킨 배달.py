import sys
import itertools

def cal(chicks):
    total_dist = 0
    for h_x, h_y in home:
        dist = 1e9
        for c_x, c_y in chicks:
            dist = min(dist, abs(h_x-c_x)+abs(h_y-c_y))
        total_dist += dist

    return total_dist

n, m = map(int, input().split())
data = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
chick = []
home = []
for i in range(n):
    for j in range(n):
        if data[i][j]==1:
            home.append([i,j])
        elif data[i][j]==2:
            chick.append([i,j])
            data[i][j] = 0
result = 1e9
for case in itertools.combinations(chick, m):
    result = min(result, cal(case))
print(result)