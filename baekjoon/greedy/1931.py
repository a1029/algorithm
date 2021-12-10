import sys
from collections import defaultdict
n = int(sys.stdin.readline())
arr = []
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    arr.append([a,b])
answer = prev = 0
arr.sort(key=lambda x: (x[1], x[0]))
for a,b in arr:
    if prev<=a:
        prev = b
        answer += 1
print(answer)