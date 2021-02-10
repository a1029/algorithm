
class Solution:

    # 자가풀이여부: O
    def my_answer(self, n, k):

        count = 0
        while n!=1:
            if n%k==0:
                n/=k
                count+=1
            else:
                n-=1
                count+=1

        print(count)


    def solution(self, n, k):

        count = 0

        while True:
            target = (n//k)*k
            count += (n-target)
            n = target

            if n<k:
                break
            count += 1
            n //= k
        count += (n-1)
        print(count)


p = Solution()
p.my_answer(25,5)
p.solution(25,5)
p.my_answer(17,4)
p.solution(17,4)
p.my_answer(25,3)
p.solution(25,3)