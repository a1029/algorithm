
def solution(files):

    result = []
    for idx,file in enumerate(files):
        num_index, tail_index = None, None
        for i in range(len(file)):
            if file[i].isdigit():
                break
            else:
                num_index = i
        for i in range(num_index+1,len(file)):
            if file[i].isdigit():
                tail_index = i
            else:
                break
        result.append([file[:num_index+1].lower(), int(file[num_index+1:tail_index+1]),idx])

    result.sort(key=lambda x:(x[0],x[1]))
    answer = []
    for x in result:
        answer.append(files[x[2]])
    return answer
