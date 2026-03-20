# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def pre(mn,node,high):
            if not node:
                return True
            if not (mn < node.val < high):
                return False
            return pre(mn,node.left,node.val) and pre(node.val,node.right,high)
        return pre(float("-inf"),root,float("inf"))