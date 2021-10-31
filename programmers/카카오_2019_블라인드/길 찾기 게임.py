import sys
sys.setrecursionlimit(10**6)
class TreeNode:
    def __init__(self, x=0, val=0, left=None, right=None):
        self.x = x
        self.val = val
        self.left = left
        self.right = right

def solution(nodeinfo):

    def insert(x, val):
        now = root
        while True:
            if x < now.x:
                if now.left is not None:
                    now = now.left
                else:
                    now.left = TreeNode(x, val)
                    break
            else:
                if now.right is not None:
                    now = now.right
                else:
                    now.right = TreeNode(x, val)
                    break

    def preorder(node):
        if node is None:
            return
        pre.append(node.val)
        preorder(node.left)
        preorder(node.right)

    def postorder(node):
        if node is None:
            return
        postorder(node.left)
        postorder(node.right)
        post.append(node.val)

    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key=lambda x:(-x[1],x[0]))

    root = TreeNode(nodeinfo[0][0], nodeinfo[0][2])
    for i in range(1, len(nodeinfo)):
        insert(nodeinfo[i][0], nodeinfo[i][2])

    pre, post = [], []
    preorder(root)
    postorder(root)
    answer = [pre, post]
    return answer
