# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def recurse(node):
            nonlocal ans
            if node:
                min_left, max_left = recurse(node.left)
                min_right, max_right = recurse(node.right)

                if min_left == max_left == min_right == max_right == -1:
                    return node.val, node.val
                
                if min_left == max_left == -1:
                    ans = max(ans, abs(node.val - min_right), abs(node.val - max_right))
                    return min(node.val, min_right), max(node.val, max_right)
                
                if min_right == max_right == -1:
                    ans = max(ans, abs(node.val - min_left), abs(node.val - max_left))
                    return min(node.val, min_left), max(node.val, max_left)

                ans = max(ans, abs(node.val - min_left), abs(node.val - max_left), abs(node.val - min_right), abs(node.val - max_right))

                return min(node.val, min_left, min_right), max(node.val, max_left, max_right)
            else:
                return -1, -1

        ans = 0
        _, _ = recurse(root)
        return ans