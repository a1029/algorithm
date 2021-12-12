def solution(strs):
    answer = 0
    for str in strs:
        stack = []
        for i in range(len(str)-1, -1, -1):
            stack.append(str[i])
            if len(stack) > 1:
                if str[i] == "A":
                    if stack[-1] == "A" and "A" not in stack[:-1]:
                        stack.clear()
                else:
                    if stack[-1] == "A":
                        stack.clear()
        if not stack:
            answer += 1
    return answer


# (AAB~|BAB~A)~
print(solution(["AABAAA", "BABABB", "BABBAAAB", "BABAAABAABBABBA"]))
print(solution(["AA", "BAB", "BAAAA", "ABBABB", "AABBBBABBAAAA"]))
print(solution(["AABAABAAB", "AABBBAABBB", "AABBBABBABABBBAAABBBABBBA"]))

print(solution(["10010111"]))
print(solution(["011000100110001"]))
print(solution(["0110001011001"]))