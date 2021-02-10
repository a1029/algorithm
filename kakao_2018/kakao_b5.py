import re
import collections
class Solution:

    def news_clustering(self, str1: str, str2: str):

        str1 = str1.lower()
        str2 = str2.lower()

        c1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
        c2 = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

        intersection = 0
        union = 0
        for c in c1:
            if c in c2:
                intersection+=1
                c2.remove(c)
            union+=1
        for c in c2:
            union+=1

        result = 1*65536 if union==0 else int(intersection/union*65536)

        print(result)

    def news_clustering2(self, str1: str, str2: str):

        str1s = [
            str1[i:i+2].lower()
            for i in range(len(str1)-1)
            if re.findall('[a-z]{2}', str1[i:i+2].lower())
        ]
        str2s = [
            str2[i:i + 2].lower()
            for i in range(len(str2) - 1)
            if re.findall('[a-z]{2}', str2[i:i + 2].lower())
        ]

        intersection = sum((collections.Counter(str1s) &
                            collections.Counter(str2s)).values())
        union = sum((collections.Counter(str1s) |
                     collections.Counter(str2s)).values())

        result = 1 if union==0 else intersection/union
        
        print(int(result*65536))

p = Solution()
p.news_clustering("FRANCE", "french")
p.news_clustering2("FRANCE", "french")
p.news_clustering("handshake", "shake hands")
p.news_clustering2("handshake", "shake hands")
p.news_clustering("aa1+aa2", "AAAA12")
p.news_clustering2("aa1+aa2", "AAAA12")
p.news_clustering("E=M*C^2", "e=m*c^2")
p.news_clustering2("E=M*C^2", "e=m*c^2")
