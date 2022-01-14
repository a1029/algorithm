import heapq
def solution(operations):
    answer = []
    q = []
    for oper in operations:
        op = oper.split(" ")
        if op[0] == "I":
            heapq.heappush(q, int(op[1]))
        else:
            if not q:
                continue
            if op[1] == "-1":
                heapq.heappop(q)
            else:
                tmp = []
                for n in q:
                    heapq.heappush(tmp, (-int(n)))
                heapq.heappop(tmp)
                q.clear()
                for n in tmp:
                    heapq.heappush(q, -n)
            
    return [0,0] if not q else [max(q), min(q)]