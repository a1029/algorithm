import sys
n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))
stack = []
answer = []
for i in range(len(towers)):
    while stack and towers[stack[len(stack)-1]] < towers[i]:
        stack.pop() 
    if stack:
        answer.append(stack[len(stack)-1]+1)
    else:
        answer.append(0)
    stack.append(i)
print(*answer)