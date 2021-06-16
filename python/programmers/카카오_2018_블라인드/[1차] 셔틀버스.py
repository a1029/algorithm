
def solution(n, t, m, timetable):

    for i in range(len(timetable)):
        hour,min = int(timetable[i][:2])*60, int(timetable[i][3:])
        timetable[i] = hour+min
    timetable.sort()
    bus = 540
    answer = 0
    for i in range(n):
        for j in range(m):
            if timetable and timetable[0] <= bus:
                answer = timetable.pop(0)-1
            else:
                answer = bus
        bus += t
    hour,min = str(answer//60).zfill(2), str(answer%60).zfill(2)
    answer = hour + ":" + min
    return answer