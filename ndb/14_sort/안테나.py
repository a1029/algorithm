# fail
def my_answer(n, data):
    data.sort()
    result = 1e9
    temp = 0
    index = 0
    for i in data:
        for j in data:
            temp += abs(i - j)
        if result >= temp:
            result = temp
            index = i
        temp = 0

    print(index)


def solution(n, data):
    data.sort()
    print(data[(n - 1) // 2])


my_answer(4, [5, 1, 7, 9])
solution(4, [5, 1, 7, 9])
