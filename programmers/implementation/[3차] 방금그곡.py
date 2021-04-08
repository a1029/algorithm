
def change(music):
    music = music.replace('C#','c')
    music = music.replace('D#','d')
    music = music.replace('F#','f')
    music = music.replace('G#','g')
    music = music.replace('A#','a')
    return music
def solution(m, musicinfos):

    m = change(m)

    for music in musicinfos:
        music = music.split(",")
        t1,t2 = music[0].split(":"), music[1].split(":")
        start = int(t1[0])*60 + int(t1[1])
        end = int(t2[0])*60 + int(t2[1])
        name,akbo = music[2], change(music[3])
        a,i = "",0
        while len(a)!=end-start:
            a += akbo[i]
            i+=1
            if i==len(akbo):
                i=0
        if m in a:
            return name



solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])
solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"])