
class Solution:

    def shuttlebus(self, n, t, m, timetable):

        for i, time in enumerate(timetable):
            hour, min = time.split(":")[0], time.split(":")[1]
            timetable[i] = int(hour)*60+int(min)
        timetable.sort()
        current = 540

        for _ in range(n):
            for _ in range(m):
                if timetable and timetable[0]<=current:
                    candidate = timetable.pop(0)-1
                else:
                    candidate = current
            current += t

        h,m = divmod(candidate, 60)
        print(str(h).zfill(2)+":"+str(m).zfill(2))

p = Solution()
p.shuttlebus(1, 1, 5, ["08:00","08:01","08:02","08:03"])
p.shuttlebus(2, 10, 2, ["09:10", "09:09", "08:00"])
p.shuttlebus(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"])
p.shuttlebus(1, 1, 5, ["00:01","00:01","00:01","00:01","00:01"])
p.shuttlebus(1, 1, 1, ["23:59"])
p.shuttlebus(10, 60, 45, ["23:59","23:59","23:59","23:59","23:59","23:59",
                          "23:59","23:59","23:59","23:59""23:59","23:59",
                          "23:59","23:59","23:59","23:59"])