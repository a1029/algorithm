import sys

n = int(input())
candidates = list(map(int, sys.stdin.readline().rstrip().split()))
b, c = map(int, input().split())

result = [0]*n

for i, candi in enumerate(candidates):
    candi -= b
    result[i] += 1
    if candi > 0:
        if candi%c == 0:
            result[i] += candi//c
        else:
            result[i] += candi//c + 1

print(sum(result))
