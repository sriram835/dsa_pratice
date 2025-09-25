

arr = [25, 35, 30, 45, 60, 50, 40]

temp = [25,30,35,40,45,50,60]

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(arr):
    postindex = len(arr)-1
    in_order = sorted(arr)

    def helper(st,end):
        nonlocal postindex

        if (st > end):
            return None

        node = Node(arr[postindex])
        postindex=-1

        in_index = in_order.index(arr[postindex])

        node.right = helper(in_index+1,end)
        node.left = helper(st,in_index-1)

        return node

    root = helper(0,len(arr)-1)

    return root


def print_level(root):
    que = []
    res = []

    que.append(root)

    while (len(que) > 0):
        curr = que.pop(0)
        
        if (curr is None):
            res.append(None)
            continue

        res.append(curr.data)
        que.append(curr.left)
        que.append(curr.right)

    return res

root = build_tree(arr)
print(print_level(root))




