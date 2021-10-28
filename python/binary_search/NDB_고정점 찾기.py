
n = int(input())
arr = list(map(int, input().split()))

start,end = 0, len(arr)-1
result = -1
while start<=end:
    mid = (start+end)//2
    if mid>arr[mid]:
        start = mid+1
    elif mid<arr[mid]:
        end = mid-1
    else:
        result = mid
        break
print(result)
