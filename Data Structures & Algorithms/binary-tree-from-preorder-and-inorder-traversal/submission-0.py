# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}
        pre_i = 0
        def build(lo, hi):
            nonlocal pre_i
            if lo >= hi: return None
            value = preorder[pre_i]; pre_i += 1
            root = TreeNode(value)
            mid = pos[value]
            root.left = build(lo, mid)
            root.right = build(mid + 1, hi)
            return root
        return build(0, len(inorder))