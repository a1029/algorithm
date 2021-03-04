import collections

# X
def my_answer(n, stages):
    counter = [0] * (n + 2)
    for stage in stages:
        counter[stage] += 1
    result = []
    length = len(stages)
    for i in range(1, len(counter) - 1):
        if length == 0:
            result.append((i, 0))
        else:
            result.append((i, counter[i] / length))
        length -= counter[i]
    result.sort(key=lambda x: -x[1])

    return [x[0] for x in result]


def solution(n, stages):
    answer = []
    length = len(stages)
    for i in range(1, n + 1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count / length

        answer.append((i, fail))
        length -= count

    answer = sorted(answer, key=lambda x: x[1], reverse=True)

    return [x[0] for x in answer]



print(my_answer(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(my_answer(4, [4, 4, 4, 4, 4]))
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
