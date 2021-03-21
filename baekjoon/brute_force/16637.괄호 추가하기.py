import sys
n = int(input())
s = input()

def cal(a,b,op):

    a = int(a)
    b = int(b)
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b


result = -sys.maxsize
def dfs(idx, res):

    global result
    if idx >= n:
        result = max(result, res)
        return

    op = s[idx-1] if idx >= 1 else '+'
    temp = cal(res, s[idx], op)
    dfs(idx+2, temp)

    if idx < n-2:

        temp = cal(s[idx], s[idx+2], s[idx+1])
        temp = cal(res, temp, op)

        dfs(idx+4, temp)


dfs(0, 0)
print(result)
