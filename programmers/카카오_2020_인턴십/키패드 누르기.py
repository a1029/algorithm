
def solution(numbers, hand):
    answer = ''
    phone = {1:(0,0),2:(0,1),3:(0,2),
             4:(1,0),5:(1,1),6:(1,2),
             7:(2,0),8:(2,1),9:(2,2),
             '*':(3,0),0:(3,1),'#':(3,2)}
    left, right = phone['*'], phone['#']
    for n in numbers:
        if n in [1,4,7]:
            answer += "L"
            left = phone[n]
        elif n in [3,6,9]:
            answer += "R"
            right = phone[n]
        else:
            cur = phone[n]
            l = abs(left[0]-cur[0]) + abs(left[1]-cur[1])
            r = abs(right[0]-cur[0]) + abs(right[1]-cur[1])
            if l==r:
                if hand=="left":
                    answer += "L"
                    left = cur
                else:
                    answer += "R"
                    right = cur
            elif l>r:
                answer += "R"
                right = cur
            elif l<r:
                answer += "L"
                left = cur
    return answer