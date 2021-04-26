
def check(stones, k, mid):

    count = 0
    for stone in stones:
        if stone-mid<=0:
            count+=1
        else:
            count=0
        if count==k:
            return False
    return True

def solution(stones, k):
    answer = 0
    start, end = 0, max(stones)
    while start <= end:
        mid = (start + end) // 2
        if check(stones, k, mid):
            start = mid+1
        else:
            end = mid-1
    return start