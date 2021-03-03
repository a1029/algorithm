
# O
def bst(data, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if mid > data[mid]:
        return bst(data, mid + 1, end)
    elif mid < data[mid]:
        return bst(data, start, mid - 1)
    else:
        return mid


def my_answer(n, data):

    start = 0
    end = len(data)
    print(bst(data, start, end-1))


my_answer(5, [-15, -6, 1, 3, 7])
my_answer(7, [-15, -4, 2, 8, 9, 13, 15])
my_answer(7, [-15, -4, 3, 8, 9, 13, 15])
