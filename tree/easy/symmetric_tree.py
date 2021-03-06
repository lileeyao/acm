# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root: return True
        return self.check(root.left, root.right)

    def check(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2 or node1.val != node2.val:
            return False
        return self.check(node1.left, node2.right) and self.check(node1.right, node2.left)
