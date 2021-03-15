import sys

def bst(target):

    start = 0
    end = len(data)-1

    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return 1
        elif data[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return 0


n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
data2 = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()

for num in data2:
    print(bst(num), end=' ')