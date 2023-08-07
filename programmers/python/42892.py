# 2019 KAKAO BLIND RECRUITMENT 길 찾기 게임
import sys 
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self):
        self.rt = None
        self.idx = None
        self.parent = None
        self.lsubtree = None
        self.rsubtree = None
        
def preorder(root, order):
    if root == None:
        return order
    order.append(root.rt)
    preorder(root.lsubtree, order)
    preorder(root.rsubtree, order)
    return order

def postorder(root, order):
    if root == None:
        return order
    postorder(root.lsubtree, order)
    postorder(root.rsubtree, order)
    order.append(root.rt)
    return order


def solution(nodeinfo):
    root = None
    nodeinfo = sorted([[node[0], node[1], i+1] for i, node in enumerate(nodeinfo)], key=lambda x: x[1], reverse=True)
    
    for i, node in enumerate(nodeinfo):
        tree = Tree()
        tree.rt = node[2]
        tree.idx = [node[0], node[1]]
        if root == None:
            root = tree
        else:
            temp = root
            while True:
                if temp.idx[0] < tree.idx[0]:
                    if temp.rsubtree == None:
                        temp.rsubtree = tree
                        break
                    else:
                        temp = temp.rsubtree
                else:
                    if temp.lsubtree == None:
                        temp.lsubtree = tree
                        break
                    else:
                        temp = temp.lsubtree
    
    answer = [preorder(root, []), postorder(root, [])]
    return answer