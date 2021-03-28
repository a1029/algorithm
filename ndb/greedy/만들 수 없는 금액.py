n = int(input())
data = list(map(int, input().split()))
data.sort()
target = 1
for num in data:
    if num<=target:
        target+=num
    else:
        print(target)
        break