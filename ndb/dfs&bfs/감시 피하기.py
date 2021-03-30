import itertools

n = int(input())
arr = [list(input().split()) for _ in range(n)]
empty = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'X':
            empty.append([i,j])

def check():
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='T':
                for k in range(j, n):
                    if arr[i][k]=='S':
                        return False
                    if arr[i][k]=='O':
                        break
                for k in range(j, -1, -1):
                    if arr[i][k]=='S':
                        return False
                    if arr[i][k]=='O':
                        break
                for k in range(i, n):
                    if arr[k][j]=='S':
                        return False
                    if arr[k][j]=='O':
                        break
                for k in range(i, -1, -1):
                    if arr[k][j]=='S':
                        return False
                    if arr[k][j]=='O':
                        break
    return True
flag = 0
for case in itertools.combinations(empty, 3):
    for i,j in case:
        arr[i][j] = 'O'
    if check():
        flag = 1
        break
    for i,j in case:
        arr[i][j] = 'X'
if flag:
    print("YES")
else:
    print("NO")