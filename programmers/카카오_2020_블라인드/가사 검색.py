import bisect

def get_count_by_range(arr, left, right):

    left_index = bisect.bisect_left(arr,left)
    right_index = bisect.bisect_right(arr,right)
    return right_index-left_index

def solution(words, queries):

    arr = [[] for _ in range(10001)]
    reversed_arr = [[] for _ in range(10001)]
    for w in words:
        arr[len(w)].append(w)
        reversed_arr[len(w)].append(w[::-1])
    for i in range(len(arr)):
        arr[i].sort()
        reversed_arr[i].sort()

    answer = []
    for q in queries:
        if q[0]!='?':
            answer.append(get_count_by_range(arr[len(q)], q.replace('?','a'), q.replace('?','z')))
        else:
            answer.append(get_count_by_range(reversed_arr[len(q)], q[::-1].replace('?','a'), q[::-1].replace('?','z')))
    return answer