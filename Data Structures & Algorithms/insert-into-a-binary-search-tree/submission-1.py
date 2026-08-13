# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        val > node => recursive all to the right
        val < node => recursive all to the left
        """
        if root is None:
            return TreeNode(val)
        current = root
        while current:
            if val > current.val:
                if current.right is None:
                    current.right = TreeNode(val)
                    return root
                current = current.right
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    return root
                current = current.left