tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(map(int, input().split()))
    
    mx = max(arr)
    cur = n-1
    answer = 0
    while arr[cur] != mx:
        i = cur - 1
        while arr[i] <= arr[cur]:
            i -= 1
        cur = i
        answer += 1
    print(answer)