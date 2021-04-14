
def check(w):
    count = 0
    for c in w:
        if c=='(':
            count+=1
        else:
            count-=1
            if count<0:
                return False
    return True

def separate(w):
    count = 0
    for i,c in enumerate(w):
        if c=='(':
            count+=1
        else:
            count-=1
        if count==0:
            return w[:i+1], w[i+1:]

def solution(p):
    if p=="":
        return ""
    u,v = separate(p)
    if check(u):
        u += solution(v)
        return u
    else:
        tmp = "("
        tmp += solution(v)
        tmp += ")"
        for c in u[1:-1]:
            if c=='(':
                tmp += ')'
            else:
                tmp += '('
        return tmp