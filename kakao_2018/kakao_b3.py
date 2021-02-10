from collections import deque

class Solution:

    def cache(self, cacheSize, cities):

        dq = deque(maxlen=cacheSize)
        time = 0
        for city in cities:
            if city in dq:
                dq.remove(city)
                dq.append(city)
                time += 1
            else:
                dq.append(city)
                time += 5

        print(time)

p = Solution()

p.cache(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
            "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
p.cache(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo",
            "Seoul", "Jeju", "Pangyo", "Seoul"])
p.cache(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
            "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
p.cache(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
            "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])
p.cache(2, ["Jeju", "Pangyo", "NewYork", "NewYork"])
p.cache(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",])
