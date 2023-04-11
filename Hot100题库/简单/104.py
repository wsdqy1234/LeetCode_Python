# 深度优先，H(root) = max(H(left), H(right)) + 1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
           return 0
        else:
           l_max = self.maxDepth(root.left)
           r_max = self.maxDepth(root.right)
           return max(l_max, r_max) + 1
            
            