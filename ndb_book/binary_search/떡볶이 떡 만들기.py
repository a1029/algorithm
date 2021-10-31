import sys

n, m = map(int, input().split())
ddeok = list(map(int, sys.stdin.readline().rstrip().split()))

start,end = 0,max(ddeok)
result = 0
while start<=end:
    mid = (start+end)//2
    total = 0
    for dd in ddeok:
        if dd>mid:
            total += dd-mid
    if total<m:
        end = mid-1
    else:
        result = mid
        start = mid+1
print(result)