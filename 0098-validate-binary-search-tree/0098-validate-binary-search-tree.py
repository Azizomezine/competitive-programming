class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((root, float("-inf"), float("inf")))
        
        while queue:
            node, min_val, max_val = queue.popleft()
            if node:
                if min_val >= node.val or node.val >= max_val:
                    return False
                if node.left:
                    queue.append((node.left, min_val, node.val))
                
                if node.right:
                    queue.append((node.right, node.val, max_val))
        return True