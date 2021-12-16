# insertion sort
def solution(numbers):
    answer = ''
    numbers = sorted(list(map(str, numbers)), reverse=True)
    i = 0
    while i < len(numbers)-1:
        j = i
        while j >= 0 and numbers[j] + numbers[j+1] < numbers[j+1] + numbers[j]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            j -= 1
        i += 1
    return str(int(''.join(numbers)))

# radix sort
def solution2(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    answer = ''.join(sorted(numbers, key=lambda x: x*3, reverse=True))
    return str(int(answer))

# merge sort
def solution3(numbers):
    def merge_sort(start, end, arr):
        if len(arr[start:end]) == 1:
            return arr[start:end]
        mid = (start + end) // 2
        arr1 = merge_sort(start, mid, arr)
        arr2 = merge_sort(mid, end, arr)
        i1, i2 = 0, 0
        result = []
        while i1 < len(arr1) and i2 < len(arr2):
            if arr1[i1] + arr2[i2] < arr2[i2] + arr1[i1]:
                result.append(arr2[i2])
                i2 += 1
            else:
                result.append(arr1[i1])
                i1 += 1
        if i1 < len(arr1):
            result.extend(arr1[i1:])
        if i2 < len(arr2):
            result.extend(arr2[i2:])
        return result
    numbers = list(map(str, numbers))
    answer = merge_sort(0, len(numbers), numbers)
    return str(int(''.join(answer)))

print(solution([6,10,2]))
print(solution([3,30,34,5,9]))