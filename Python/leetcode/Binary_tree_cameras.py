# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cam=0
        covered=set()
        def dfs(node,parent):
            if node:
                dfs(node.left,node)
                dfs(node.right,node)
                if parent is None and node not in covered or node.left not in covered or node.right not in covered:
                    self.cam+=1
                    covered.add(node)
                    covered.add(parent)
                    covered.add(node.left)
                    covered.add(node.right)
        covered.add(None)
        dfs(root,None)
        return self.cam