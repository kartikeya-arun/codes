"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        nodes_queue=deque()
        nodes_queue.append(root)
        
        while nodes_queue:
            size=len(nodes_queue)
            for i in range(size):
                node=nodes_queue.pop()
                if i<(size-1):
                    node.next=nodes_queue[-1]
                if node.left:
                    nodes_queue.appendleft(node.left)
                if node.right:
                    nodes_queue.appendleft(node.right)
                    
        return root