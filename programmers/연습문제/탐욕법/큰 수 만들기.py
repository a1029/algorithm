
# https://programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    answer = ''
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            k -= 1
            stack.pop()
        stack.append(n)

    while k>0:
        k -= 1
        stack.pop()
    return ''.join(stack)

print(solution("1000", 1)) # 100