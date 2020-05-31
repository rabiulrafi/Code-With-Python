class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.data,end = " ")
        inOrder(root.right)

def insert(temp,key):
    q=[]
    q.append(temp)
    while(len(q)):
        temp = q[0]
        q.pop(0)
        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)
        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)

# root= Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left  = Node(4)
# root.left.right  = Node(5)
# preOrder(root)

def buildTree(i):
    if i < len(values):
        return Node(values[i], left=buildTree((i+1)*2-1), right=buildTree((i+1)*2))

values = [1,2,3,4,5]
tree = buildTree(0)
print(inOrder(tree))
insert(tree,8)
print(inOrder(tree))