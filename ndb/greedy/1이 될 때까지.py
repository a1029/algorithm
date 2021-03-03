
# O
def my_answer(n, k):

    count = 0
    while n!=1:
        if n%k==0:
            n/=k
            count+=1
        else:
            n-=1
            count+=1

    print(count)


def solution(n, k):

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


my_answer(25,5)
solution(25,5)
my_answer(17,4)
solution(17,4)
my_answer(25,3)
solution(25,3)