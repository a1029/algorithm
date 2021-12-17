import math
for _ in range(int(input())):
    n = int(input())
    target = 2
    while True:
        target += 1
        if math.gcd(n-1-target, target) != 1:
            continue
        print(n-1-target, target, 1)
        break
