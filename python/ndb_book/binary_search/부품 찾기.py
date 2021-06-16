import sys
import bisect
n = int(input())
part = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
ask_part = list(map(int, sys.stdin.readline().rstrip().split()))

part.sort()
for ask in ask_part:
    index = bisect.bisect(part, ask)
    if part[index-1]!=ask:
        print("no", end=' ')
    else:
        print("yes", end=' ')