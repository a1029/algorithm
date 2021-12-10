def solution(s):
    answer = []
    for string in s:
        stack = []
        count = 0
        for c in string:
            stack.append(c)
            if c == '0' and stack[-3:] == ['1', '1', '0']:
                count += 1
                del stack[-3:]
        idx = ''.join(stack).rfind('0')
        if idx == -1:
            answer.append('110'*count + ''.join(stack))
        else:
            answer.append(''.join(stack[:idx+1]) + '110'*count + ''.join(stack[idx+1:]))
    return answer

print(solution(["1110","100111100","0111111010"]))
