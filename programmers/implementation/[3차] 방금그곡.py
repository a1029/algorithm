
def change(music):
    music = music.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    return music

def solution(m, musicinfos):
    answer = []
    m = change(m)
    for i, infos in enumerate(musicinfos):
        info = infos.split(",")
        start, end, name, akbo = info[0].split(":"), info[1].split(":"), info[2], change(info[3])
        time = int(end[0])*60 + int(end[1]) - (int(start[0])*60 + int(start[1]))
        if len(akbo) >= time:
            melody = akbo[0:time]
        else:
            a,b = divmod(time, len(akbo))
            melody = akbo*a + akbo[0:b]
        if m in melody:
            answer.append([i, time, name])
    if answer:
        answer.sort(key=lambda x: (-x[1], x[0]))
        return answer[0][2]
    else:
        return "(None)"
