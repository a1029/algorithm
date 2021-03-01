import bisect


# fail
def count_by_range(a, left_value, right_value):
    left = bisect.bisect_left(a, left_value)
    right = bisect.bisect_right(a, right_value)
    return right - left


def solution(words, queries):
    array = [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]
    result = []
    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for query in queries:
        if query[0] != '?':
            res = count_by_range(array[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
        else:
            res = count_by_range(reversed_array[len(query)], query[::-1].replace('?', 'a'),
                                 query[::-1].replace('?', 'z'))

        result.append(res)

    print(result)


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["fro??", "????o", "fr???", "fro???", "pro?"])
