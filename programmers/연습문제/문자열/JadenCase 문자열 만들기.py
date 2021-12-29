def solution(s):
    answer = ''
    a = []
    for c in s.split(" "):
        if c != "":
            a.append(c[0].upper() + c[1:].lower())
        else:
            a.append("")
    return ' '.join(a)

print(solution("3people unFollowed me"))
print(solution("3people  unFollowed me"))
print(solution("aaaaa aaa"))
print(solution(" adgagd 3eagdag ")==" Adgagd 3eagdag ")