import collections

def solution(cacheSize, cities):
    answer = 0
    q = collections.deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in q:
            answer += 1
            q.remove(city)
            q.append(city)
        else:
            answer += 5
            q.append(city)
    return answer
