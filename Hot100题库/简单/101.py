# 递归解决，左边的左边=右边的右边 and 左边的右边=右边的左边
# 跳出条件：1. 左边与右边均为None——返回True
#         2. 左边与右边有一个为None但另一个不为None——返回False
#         3. 左边与右边不相等——返回False
# 如果当前左边=右边，则继续DFS深度优先，直到搜索到叶子结点所指的None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(l, r):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False
            if l.val != r.val:
                return False
            return dfs(l.left, r.right) and dfs(l.right, r.left)

        return dfs(root.left, root.right)