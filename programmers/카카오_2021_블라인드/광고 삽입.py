

def to_sec(x):
    t = x.split(':')
    return int(t[0])*3600 + int(t[1])*60 + int(t[2])

def to_str(x):
    m,s = divmod(x, 60)
    h,m = divmod(m, 60)
    return str(h).zfill(2)+':'+str(m).zfill(2)+':'+str(s).zfill(2)

def solution(play_time, adv_time, logs):

    pt = to_sec(play_time)
    at = to_sec(adv_time)
    tt = [0]*360001
    for log in logs:
        start, end = map(to_sec, log.split('-'))
        tt[start] += 1
        tt[end] -= 1

    for i in range(1, pt):
        tt[i] += tt[i-1]
    for i in range(1, pt):
        tt[i] += tt[i-1]

    mt = 0
    answer = 0
    for i in range(at-1, pt):
        if i>=at:
            if mt < tt[i]-tt[i-at]:
                mt = tt[i]-tt[i-at]
                answer = i-at+1
        else:
            if mt < tt[i]:
                mt = tt[i]
                answer = i-at+1
    return to_str(answer)


solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])