# https://programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    answer = []
    for i in range(len(prices)):
        count = 0
        flag = False
        for j in range(i+1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                answer.append(count)
                flag = True
                break
        if not flag:
            answer.append(count)
    return answer

def solution2(prices):
    answer = [0]*len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            answer[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    
    while stack:
        i = stack.pop()
        answer[i] = len(prices)-1-i
    return answer

print(solution2([1, 2, 3, 2, 3]))