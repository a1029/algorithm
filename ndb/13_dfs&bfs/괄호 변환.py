
# fail
def separate(w):
    index = 0
    for i in range(len(w)):
        if w[i] == '(':
            index += 1
        else:
            index -= 1
        if index == 0:
            return w[:i + 1], w[i + 1:]


def check(w):
    count = 0
    for c in w:
        if c == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def solution(w):
    if w == "":
        return ""
    answer = ""
    u, v = separate(w)
    if check(u):
        answer = u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer


print(solution("(()())()")) # (()())()
print(solution(")("))       # ()
print(solution("()))((()")) # ()(())()
