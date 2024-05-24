# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        sub =[]
        def dfs(root, sub):
            if not root:
                return
            if root.left:
                dfs(root.left, sub)
            sub.append(root.val)
            if root.right:
                dfs(root.right, sub)
        
        dfs(root, sub)
        
        return sub[k-1]