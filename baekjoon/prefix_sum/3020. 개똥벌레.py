import bisect
import sys

n, h = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(sys.stdin.readline().rstrip()))

arr1 = [data[i] for i in range(n) if i % 2 == 0]
arr2 = [data[i] for i in range(n) if i % 2 == 1]
arr1.sort()
arr2.sort()

result = []
for i in range(h, 0, -1):
    a = len(arr1) - bisect.bisect_left(arr1, i)
    b = len(arr2) - bisect.bisect_right(arr2, h - i)
    result.append(a + b)

print(min(result), result.count(min(result)))
