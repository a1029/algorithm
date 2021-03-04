import bisect


# X
def my_answer(n, x, data):
    a = bisect.bisect_left(data, x)
    b = bisect.bisect_right(data, x)
    if b - a != 0:
        print(b - a)
    else:
        print(-1)


def solution(n, x, data):
    def first(target, start, end):

        if start > end:
            return None
        mid = (start + end) // 2
        if (mid == 0 or target > data[mid - 1]) and data[mid] == target:
            return mid
        elif data[mid] >= target:
            return first(target, start, mid - 1)
        else:
            return first(target, mid + 1, end)

    def last(target, start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        if (mid == n - 1 or target < data[mid + 1]) and data[mid] == target:
            return mid
        elif data[mid] > target:
            return last(target, start, mid - 1)
        else:
            return last(target, mid + 1, end)

    a = first(x, 0, n - 1)
    b = last(x, 0, n - 1)

    if a is None or b is None:
        print(-1)
    else:
        print(b - a + 1)


my_answer(7, 2, [1, 1, 2, 2, 2, 2, 3])
my_answer(7, 4, [1, 1, 2, 2, 2, 2, 3])
solution(7, 2, [1, 1, 2, 2, 2, 2, 3])
solution(7, 4, [1, 1, 2, 2, 2, 2, 3])
