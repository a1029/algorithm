
def rotate(x1,y1,x2,y2,graph):

    x = int(1e9)
    a,b,c,d = graph[x1][y2],graph[x2][y2],graph[x2][y1],graph[x1][y1]
    for i in range(y2,y1,-1):
        graph[x1][i] = graph[x1][i-1]
    for i in range(x2,x1,-1):
        graph[i][y2] = graph[i-1][y2]
    for i in range(y1,y2):
        graph[x2][i] = graph[x2][i+1]
    for i in range(x1,x2):
        graph[i][y1] = graph[i+1][y1]
    graph[x1+1][y2] = a
    graph[x2][y2-1] = b
    graph[x2-1][y1] = c

    for i in range(y1,y2+1):
        x = min(x,graph[x1][i],graph[x2][i])
    for i in range(x1,x2+1):
        x = min(x,graph[i][y1],graph[i][y2])

    return x


def solution(rows, columns, queries):
    answer = []
    graph = [[(i+1)+(j*columns) for i in range(columns)] for j in range(rows)]
    for a,b,c,d in queries:
        answer.append(rotate(a-1,b-1,c-1,d-1,graph))
    return answer