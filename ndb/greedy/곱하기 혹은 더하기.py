
# success
def my_answer(s):

    arr = [int(x) for x in s]

    result = 0
    for i in range(len(arr)):
        result = max(result+arr[i], result*arr[i])

    print(result)


def solution(s):

    arr = [int(x) for x in s]

    result = arr[0]
    for i in range(1, len(arr)):
        if arr[i] <= 1 or result <= 1:
            result += arr[i]
        else:
            result *= arr[i]
    print(result)


my_answer("02984") # 576
my_answer("567") # 210
my_answer("1111") # 4
my_answer("1212") # 8
my_answer("9991") # 730
my_answer("0203") # 6
solution("02984") # 576
solution("567") # 210
solution("1111") # 4
solution("1212") # 8
solution("9991") # 730
solution("0203") # 6