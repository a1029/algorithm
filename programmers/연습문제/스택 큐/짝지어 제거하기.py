def solution(s):
    answer = -1
    stack = [s[0]]
    for i in range(1, len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    return 0 if stack else 1        
print(solution('baabaa'))
print(solution('cdcd'))