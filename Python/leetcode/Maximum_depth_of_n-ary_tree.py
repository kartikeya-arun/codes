"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        # BFS
        # depth=0
        # q=deque()
        # q.append(root)
        # while q:
        #     for i in range(len(q)):
        #         node=q.popleft()
        #         for child in node.children:
        #             q.append(child)
        #     depth+=1
        # return depth
        
        # DFS
        maxDepth=0
        for child in root.children:
            maxDepth=max(maxDepth,self.maxDepth(child))
        return maxDepth+1