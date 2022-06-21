# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        def dfs(node,curSum,lst):
            if not node:
                return
            curSum+=node.val
            lst=lst+[node.val]
            if not node.left and not node.right:
                if curSum==targetSum:
                    ans.append(lst)
            dfs(node.left,curSum,lst)
            dfs(node.right,curSum,lst)
        dfs(root,0,[])
        return ans