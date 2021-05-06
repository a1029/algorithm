import collections
import sys
sys.setrecursionlimit(10**6)

def find_parent(room, parent):
    if parent[room]==0:
        parent[room]=room+1
        return parent[room]
    parent[room] = find_parent(parent[room], parent)
    return parent[room]

def solution(k, room_number):

    answer = []
    parent = collections.defaultdict(int)
    for room in room_number:
        if parent[room]==0:
            answer.append(room)
            parent[room] = room+1
        else:
            answer.append(find_parent(room, parent)-1)
    return answer