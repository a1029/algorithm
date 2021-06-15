
import collections

def solution(arr):

    counter = collections.Counter(arr)
    res = counter.most_common()
    res.sort(key=lambda x:x[0])
    answer = []
    for a,b in res:
        if b>1:
            answer.append(b)
    if answer:
        print(answer)
    else:
        print([-1])

solution([1,2,3,3,3,3,4,4])
solution([3,2,4,4,2,5,2,5,5])
solution([3,5,7,9,1])