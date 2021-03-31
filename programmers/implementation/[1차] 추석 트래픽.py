
def solution(lines):

    for i in range(len(lines)):
        a = lines[i].split(" ")[1].split(":")
        b = lines[i].split(" ")[2][:-1]
        end = round(float(a[0])*3600 + float(a[1])*60 + float(a[2]), 3)
        start = round(end - float(b) + float(0.001), 3)
        lines[i] = [start,end]

    result = []
    for a,b in lines:
        c = round(float(b + 1 - 0.001), 3)
        count = 0
        for start,end in lines:
            if b<=end<=c:
                count+=1
            elif b<=start<=c:
                count+=1
            elif start<=b and c<=end:
                count+=1
        result.append(count)
    answer = max(result)
    return answer