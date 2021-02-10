import re

class Solution:

    def score(self, input: str):

        p = re.compile("(\d+)([SDT]+)([*#]*)")
        m = p.findall(input)

        result = []
        for i,round in enumerate(m):

            if round[1]=='S':
                num = int(round[0])
            elif round[1]=='D':
                num = int(round[0])**2
            elif round[1]=='T':
                num = int(round[0])**3

            if round[2]=='*':
                if i>=1:
                    result[i-1] *= 2
                num *= 2
            elif round[2]=='#':
                num *= -1

            result.append(num)

        print(sum(result))


p = Solution()

p.score("1S2D*3T")
p.score("1D2S#10S")
p.score("1D2S0T")
p.score("1S*2T*3S")
p.score("1D#2S*3S")
p.score("1T2D3D#")
p.score("1D2S3T*")