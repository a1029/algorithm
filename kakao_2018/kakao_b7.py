import collections
import re
class Solution:

    def solution(self, lines):

        window = collections.defaultdict(float)
        log = collections.defaultdict(float)
        logs = []
        result = 0

        for l in lines:

            # 로그 처리 완료 시간 finish, 계산하기 쉽게 초 단위로
            finish = l.split(" ")[1].split(":")
            finish = float(finish[0])*3600 + float(finish[1])*60 + float(finish[2])
            log['end'] = finish

            # 로그 처리시간 elapsed, 로그 처리 시작 시간을 구하기 위해서
            elapsed = float(l.split(" ")[2][:-1])
            log['start'] = log['end']-elapsed+0.001

            logs.append(log.copy())

        for l in logs:

            # 윈도우의 시작구간을 각 로그의 끝범위로, 끝구간은 시작구간 1초 이후
            window['start'] = l['end']
            window['end'] = round(window['start']+1.000-0.001, 3)

            count = 0

            # 각 로그가 윈도우에 포함되기 위한 조건 3가지
            for log in logs:
                if window['start'] <= log['end'] <= window['end']:
                    count+=1
                elif window['start'] <= log['start'] <= window['end']:
                    count+=1
                elif log['start']<=window['start'] and log['end']>=window['end']:
                    count+=1

            result = max(result, count)

        print(result)


p = Solution()

p.solution(["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"])
p.solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"])
p.solution([
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
])
