class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root]
        
        while stack:
            temp = stack.pop()
            
            if temp:
                ans.append(temp.val)
                stack.append(temp.right)
                stack.append(temp.left)
                
        return ans