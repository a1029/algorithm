import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = []
stack = []
for num in arr[::-1]:
    while stack and stack[len(stack)-1] <= num:
        stack.pop()
    if stack: answer.append(stack[len(stack)-1])
    else: answer.append(-1)
    stack.append(num)
print(*answer[::-1])

stack = [0]
for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)

# 5 3 7 9 1
# 7 7 9 -1 -1