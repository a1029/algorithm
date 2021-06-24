import collections

def solution(param0):

    file_dict = collections.defaultdict(int)
    for path in param0:
        path = path.split('/')
        path = path[-1].split('.')
        name, extension = path[0][0], path[1]
        filename = name + '.' + extension
        file_dict[filename] += 1
    answer = []
    for k,v in file_dict.items():
        if v>=2:
            answer.append(k)
            answer.append(v)

    return answer

solution(['/a/a_v2.x','/b/a.x','/c/t.z','/d/a/t.x','/e/z/t_v1.z','/k/k/k/a_v9.x'])
solution(['/t.z','/z/z_v2.z','/a.z','/d/b.z','/d/a/t.z'])
solution(['/t.z','/b/b.z','/a.z','/e/k.z','/d/a/x_v2.z'])
