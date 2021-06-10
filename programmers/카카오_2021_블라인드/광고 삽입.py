import collections


def get_second(data):
    times = data.split(':')
    return int(times[0])*3600 + int(times[1])*60 + int(times[2])


def solution(play_time, adv_time, logs):

    play_time_sec = get_second(play_time)
    adv_time_sec = get_second(adv_time)
    logs_start_sec = []
    logs_end_sec = []
    for log in logs:
        logs_start_sec.append(get_second(log.split('-')[0]))
        logs_end_sec.append(get_second(log.split('-')[1]))

    total_time = collections.defaultdict(int)
    for i in range(len(logs)):
        total_time[logs_start_sec[i]] = total_time[logs_start_sec[i]] + 1
        total_time[logs_end_sec[i]] = total_time[logs_end_sec[i]] - 1

    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i-1]

    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i-1]

    max_time = 0
    for i in range(adv_time_sec-1, play_time_sec):
        if i:
            max_time = max(max_time, total_time[i] - total_time[i-at])
        else:
            max_time = max(max_time, total_time[i])

    h,mod = divmod(max_time, 60)
    m,s = divmod(mod, 60)
    answer = str(h)+':'+str(m)+':'+str(s)
    print(answer)
    return answer


solution("02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
solution("99:59:59","25:00:00",["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
solution("50:00:00","50:00:00",["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])