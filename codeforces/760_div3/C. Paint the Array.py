import math
tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    even, odd = 0, 0
    for i in range(n):
        if i%2==0:
            even = math.gcd(even, arr[i])
        else:
            odd = math.gcd(odd, arr[i])

    a,b = 0,0
    for i in range(1, n, 2):
        if arr[i]%even==0:
            a = 1
            break
    for i in range(0, n, 2):
        if arr[i]%odd==0:
            b = 1
            break
    if a and b:
        print(0)
    elif a==0:
        print(even)
    else:
        print(odd)
