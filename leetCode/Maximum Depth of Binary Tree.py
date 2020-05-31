class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            L= self.maxDepth(root.left)+1
            R =self.maxDepth(root.right)+1
            return max(L,R)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.maxDepth(root))
