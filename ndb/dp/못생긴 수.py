

# fail
def check(i):

    while i!=1:
        if i%2==0:
            i/=2
        elif i%3==0:
            i/=3
        elif i%5==0:
            i/=5
        else:
            return False
    return True


def my_answer(n):

    dp = []
    for i in range(1, 100000000):
        if check(i):
            dp.append(i)

    print(dp[n-1])


def solution(n):

    ugly = [0] * n
    ugly[0] = 1
    i2 = i3 = i5 = 0
    next2, next3, next5 = 2, 3, 5

    for l in range(1, n):
        print(ugly)
        ugly[l] = min(next2, next3, next5)
        if ugly[l] == next2:
            i2 += 1
            next2 = ugly[i2] * 2
        if ugly[l] == next3:
            i3 += 1
            next3 = ugly[i3] * 3
        if ugly[l] == next5:
            i5 += 1
            next5 = ugly[i5] * 5


    print(ugly[n-1])


#my_answer(1000)
#my_answer(4)
solution(10)
#solution(4)