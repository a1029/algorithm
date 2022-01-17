import heapq
def solution(n, works):
    if sum(works) < n:
        return 0
    
    heap = []
    for w in works:
        heapq.heappush(heap, -w)
    
    while n != 0:
        maxv = heapq.heappop(heap)
        maxv += 1
        n -= 1
        heapq.heappush(heap, maxv)
        
    return sum([x*x for x in heap])