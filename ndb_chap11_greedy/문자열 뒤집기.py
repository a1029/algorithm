from typing import List


# 자가풀이여부: O
def my_answer(s):
    c0, c1 = 0, 0
    boolean = True

    for n in s:
        if n == '0' and boolean == True:
            boolean = False
            c0 += 1
        elif n == '1' and boolean == False:
            boolean = True
            c1 += 1
    print(min(c0, c1))


def solution(s):
    c0, c1 = 0, 0
    if s[0] == '1':
        c0 += 1
    else:
        c1 += 1

    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            if s[i + 1] == '1':
                c0 += 1
            else:
                c1 += 1
    print(min(c0, c1))


my_answer("0001100")  # 1
my_answer("00011010")  # 2
solution("0001100")  # 1
solution("00011010")  # 2

