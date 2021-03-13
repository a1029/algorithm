import itertools

n = int(input())
data = list(map(int, input().split()))

result = 0
for case in itertools.permutations(data):

    tmp = 0
    for i in range(n-1):
        tmp += abs(case[i]-case[i+1])
    result = max(result, tmp)

print(result)