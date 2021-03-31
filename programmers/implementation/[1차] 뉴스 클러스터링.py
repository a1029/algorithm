def solution(str1, str2):

    str1 = str1.lower()
    str2 = str2.lower()
    s1 = [str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    intersection, union = 0,0

    for c in s1:
        if c in s2:
            intersection += 1
            s2.remove(c)
        union += 1
    for c in s2:
        union += 1

    return int(intersection/union*65536) if union!=0 else 1*65536