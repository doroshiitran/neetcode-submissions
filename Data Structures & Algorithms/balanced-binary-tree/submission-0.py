# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        go for every node in each leaf, when meeting null in 2 children return current depth
        compare 2 leaf depth
        """
        self.balanced=True
        def dfs(root):
            if root is None:
                return 0
            left_depth=dfs(root.left)
            right_depth=dfs(root.right)
            if abs(left_depth-right_depth)>1:
                self.balanced=False
            return 1 + max(left_depth,right_depth)
        dfs(root)
        return self.balanced