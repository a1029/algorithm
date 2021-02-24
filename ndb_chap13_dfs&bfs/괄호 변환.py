
# fail
def separate(w):
    count = 0
    for i in range(len(w)):
        if w[i] == "(":
            count += 1
        else:
            count -= 1
        if count == 0:
            u = w[:i + 1]
            v = w[i + 1:]
            return u, v


def check(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def solution(w):

    answer = ''
    if w == '':
        return answer

    u,v = separate(w)
    if check(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer


print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))

