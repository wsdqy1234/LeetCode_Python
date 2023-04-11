# 前序遍历：根-左-右
# 中序遍历：左-根-右
# 后序遍历：左-右-根

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def dfs(root): # DFS: 深度优先搜索
            if root is None: return # 叶子，返回空
            dfs(root.left) # 左
            res.append(root.val) # 中
            dfs(root.right) # 右
        dfs(root)
        return res