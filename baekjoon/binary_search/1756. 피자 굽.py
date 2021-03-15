import sys
import bisect

d, n = map(int, input().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))
data2 = list(map(int, sys.stdin.readline().rstrip().split()))
visit = [False]*len(data)

for i in range(1, len(data)):
    if data[i] > data[i-1]:
        data[i] = data[i-1]

def bst(arr, target):

    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            start = mid + 1
        else:
            end = mid - 1

