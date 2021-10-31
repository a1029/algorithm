

def solution(n, z, roads, queries):
    graph = [[]*n for _ in range(n)]
    edges = []
    for a,b,c in roads:
        graph[a].append([b,c])
        edges.append(c)

    answer = []
    for query in queries:
        res = 0
        if query==0:
            res = 0
        elif query%z==0:
            res += query//z
        elif query%z!=0 and query%z in edges:
            res += query//z
            res += bfs(query%z)
        elif query%z!=0 and query%z not in edges:
            res += bfs(query    )
        answer.append(res)

    return answer

solution(5,5,[[1,2,3],[0,3,2]],[0,1,2,3,4,5,6])