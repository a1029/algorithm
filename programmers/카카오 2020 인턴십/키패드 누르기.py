
def solution(numbers, hand):

    phone = {1:(0,0), 2:(0,1), 3:(0,2),
             4:(1,0), 5:(1,1), 6:(1,2),
             7:(2,0), 8:(2,1), 9:(2,2),
             '*':(3,0),0:(3,1),'#':(3,2)}
    left, right = phone['*'], phone['#']

    answer = ""
    for n in numbers:
        if n in [1,4,7]:
            answer += "L"
            left = phone[n]
        elif n in [3,6,9]:
            answer += "R"
            right = phone[n]
        else:
            pos = phone[n]
            l_dist = abs(left[0]-pos[0]) + abs(left[1]-pos[1])
            r_dist = abs(right[0]-pos[0]) + abs(right[1]-pos[1])
            if l_dist < r_dist:
                answer += "L"
                left = phone[n]
            elif l_dist > r_dist:
                answer += "R"
                right = phone[n]
            else:
                if hand=="left":
                    answer += "L"
                    left = phone[n]
                else:
                    answer += "R"
                    right = phone[n]
    return answer
