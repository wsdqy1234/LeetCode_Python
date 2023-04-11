# 把问题拆分成 1.求root节点的深度； 2. 使用全局监听器，找所有节点的左深度与右深度之和的最大值

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_d = 0 # 定义全局变量进行监听
        def depth(root):
            if root is None: return 0
            L = depth(root.left)
            R = depth(root.right)
            if (L+R) > self.max_d: self.max_d = L + R #监听任意节点作为root节点时，左深度与右深度之和的最大值
            return max(L, R) + 1
        depth(root)
        return self.max_d