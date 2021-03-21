
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
result = 0
for i in range(n):
    result = max(result, min(data[i]))

print(result)