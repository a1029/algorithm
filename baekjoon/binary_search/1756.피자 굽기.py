import sys
    
d, n = map(int, input().split())
oven = list(map(int, sys.stdin.readline().rstrip().split()))
pizza = list(map(int, sys.stdin.readline().rstrip().split()))
visit = [False]*len(oven)

for i in range(1, d):
    if oven[i] > oven[i-1]:
        oven[i] = oven[i-1]

idx = 0
for i in range(d-1, -1, -1):
    if pizza[idx] <= oven[i]:
        visit[idx] = 1 + i
        idx += 1
    if idx==n:
        break

if idx==n:
    print(visit[idx-1])
else:
    print(0)