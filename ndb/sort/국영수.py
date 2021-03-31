
n = int(input())
arr = []
for _ in range(n):
    a = list(input().split())
    a[1],a[2],a[3] = int(a[1]),int(a[2]),int(a[3])
    arr.append(a)

arr.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for i in arr:
    print(i[0])