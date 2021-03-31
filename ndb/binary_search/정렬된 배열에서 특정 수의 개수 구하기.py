import bisect
import sys
n,x = map(int, input().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

left = bisect.bisect_left(arr,x)
right = bisect.bisect_right(arr,x)
if left==right:
    print(-1)
else:
    print(right-left)