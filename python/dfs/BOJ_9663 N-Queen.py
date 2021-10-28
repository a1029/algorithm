
n = int(input())
result = 0
row = [0]*n

def check(c):

    for i in range(c):
        if row[c]==row[i] or abs(row[c]-row[i]) == c-i:
            return False
    return True


def dfs(c):
    global result

    if c == n:
        result += 1
        return

    for i in range(n):
        row[c] = i
        if check(c):
            dfs(c+1)

dfs(0)
print(result)

