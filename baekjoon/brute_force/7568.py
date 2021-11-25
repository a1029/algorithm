arr = []
n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]
result = []
for i,[a,b] in enumerate(arr):
    count = 0
    for j,[c,d] in enumerate(arr):
        if i==j:
            continue
        if a<c and b<d:
            count += 1
    result.append(str(count+1))

print(' '.join(result))