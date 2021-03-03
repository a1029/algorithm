

# X
def solution(n, c, data):
    data.sort()

    start = 1
    end = data[-1] - data[0]
    result = 0

    while start <= end:
        mid = (start + end) // 2
        value = data[0]
        count = 1
        for i in range(1, n):
            if data[i] >= value + mid:
                value = data[i]
                count += 1
        if count >= c:
            start = mid + 1
            result = mid
        else:
            end = mid - 1

    print(result)


solution(5, 3, [1, 2, 8, 4, 9])
