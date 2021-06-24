
def solution(param0):

    i = 0
    tmp = ''
    answer = []
    for i in range(len(param0)):
        if len(''.join(answer))>=128:
            print("HALT")
            return

        if len(tmp)==8:
            answer.append(tmp)
            i = 0
            tmp = ''

        if param0[i]=='BOOL':
            tmp += '#'
            i += 1
        elif param0[i]=='SHORT':
            if i%2==0:
                tmp += '##'
                i += 2
            else:
                while i%2!=0:
                    tmp += '.'
                    i+=1
        elif param0[i]=='FLOAT':
            if i%4==0:
                tmp += '####'
                i += 4
            else:
                while i%4!=0:
                    tmp += '.'
                    i+=1
        elif s=='INT':
            if i!=0:
                while len(tmp)!=8:
                    tmp += '.'
                answer.append(tmp)
                answer.append('########')
        else:
            if i!=0:
                while len(tmp)!=8:
                    tmp += '.'
                answer.append(tmp)
                answer.append('########,########')

    answer = ','.join(answer)
    return answer