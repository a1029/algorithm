
def possible(answer):
    for x,y,stuff in answer:
        if stuff==0:
            if y==0 or [x,y-1,0] in answer or [x-1,y,1] in answer or [x,y,1] in answer:
                continue
            return False
        else:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for x,y,stuff,op in build_frame:
        if op==1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
        else:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
    return sorted(answer)
