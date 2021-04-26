import collections
import sys
sys.setrecursionlimit(10**6)
def find(parent, room):
    if parent[room]==0:
        parent[room] = room+1
        return room+1
    parent[room] = find(parent, parent[room])
    return parent[room]
def solution(k, room_number):
    answer = []
    parent = collections.defaultdict(int)
    for room in room_number:
        if parent[room]==0:
            parent[room] = room+1
            answer.append(room)
        else:
            answer.append(find(parent, room)-1)
    return answer