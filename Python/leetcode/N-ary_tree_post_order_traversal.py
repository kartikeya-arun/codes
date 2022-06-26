"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack=[]
        answer=deque()
        if not root:
            return answer
        stack.append(root)
        while len(stack)!=0:
            node=stack.pop()
            answer.appendleft(node.val)
            for child in node.children:
                stack.append(child)
        return answer