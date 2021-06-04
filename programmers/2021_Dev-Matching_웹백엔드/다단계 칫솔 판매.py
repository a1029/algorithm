
def solution(enroll, referral, seller, amount):

    answer = [0]*len(enroll)
    enroll_num = dict(zip(enroll,range(len(enroll))))

    for i in range(len(seller)):
        now = seller[i]
        profit = amount[i]*100
        while True:
            num = enroll_num[now]
            div = profit // 10
            answer[num] += profit-div
            profit = div
            now = referral[num]
            if now=='-' or div==0:
                break
    return answer