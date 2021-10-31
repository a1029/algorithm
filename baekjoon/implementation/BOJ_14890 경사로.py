def check(line):
    install = [False for _ in range(n)]
    for i in range(n-1):
        if line[i] == line[i+1]:
            continue
        if abs(line[i]-line[i+1]) > 1:
            return False
        if line[i] > line[i+1]:
            temp = line[i+1]
            for j in range(i+1, i+1+l):
                if 0 <= j < n:
                    if line[j] != temp:
                        return False
                    if install[j]:
                        return False
                    install[j] = True
                else:
                    return False
        else:
            temp = line[i]
            for j in range(i, i-l, -1):
                if 0 <= j < n:
                    if line[j] != temp:
                        return False
                    if install[j]:
                        return False
                    install[j] = True
                else:
                    return False
    return True

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = list(map(list, zip(*arr)))
result = 0
for i in arr:
    if check(i):
        result += 1
for j in arr2:
    if check(j):
        result += 1
print(result)
